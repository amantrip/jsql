import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.Writer;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;
import jsonworker.JsonWorker;
import java.util.ArrayList;
import org.json.simple.JSONObject;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

// JsonList is a ArrayList of JsonWorker objects
public class JsonList {

    ArrayList<JsonWorker> jsonList = new ArrayList<JsonWorker>();
    private Pattern mPattern = Pattern.compile("/^(select)\s+([a-z0-9_\,\.\s\*]+)\s+from\s+([a-z0-9_\.]+)(?: where\s+\((.+)\))?\s*(?:order\sby\s+([a-z0-9_\,]+))?\s*(asc|desc|ascnum|descnum)?\s*(?:limit\s+([0-9_\,]+))?/i");

    // Constructor takes in an array of JsonWorker objects and creates the 
    // ArrayList of out of them    
    public JsonList(JsonWorker[] list){
        for(int i = 0; i<list.length; i++){
            jsonList.add(list[i]);
        }
    }

    // helper function that parses string into array of JsonWorker objects
    JsonWorker[] parseJsonList(String str) throws ParseException{
        String parseableString = "[" + str.substring(1, str.length() - 2) + "]";
         JSONParser parser=new JSONParser();
         try{
            Object obj = parser.parse(parseableString);
            JSONArray jsonArray = (JSONArray)obj;
            JsonWorker[] arr = new JsonWorker[jsonArray.size()];
            for(int i = 0; i<arr.length; i++){
                arr[i] = new JsonWorker(jsonArray.get(i).toString());
            }
            return arr;
         }catch(ParseException pe){
            System.out.println("position: " + pe.getPosition());
            System.out.println(pe);
            throw pe;
         }
    }

    // parses the text in fileName and returns the equivalent JsonList object 
    public JsonList readFile(String fileName) throws FileNotFoundException, IOException, ParseException{
        String in;
        BufferedReader br = new BufferedReader(new FileReader(fileName));
         try {
             StringBuilder sb = new StringBuilder();
             String line = br.readLine();

             while (line != null) {
                 sb.append(line);
                 sb.append(System.lineSeparator());
                 line = br.readLine();
             }
             in = sb.toString();
         } finally {
             br.close();
         }
                  
         return new JsonList(parseJsonList(in));
    }
    
    // converts jsonList to a string and writes it to fileName
    public void writeToFile(String fileName){
        Writer writer = null;

        try {
            writer = new BufferedWriter(new OutputStreamWriter(
                  new FileOutputStream(fileName), "utf-8"));
            writer.write(this.toString());
        } catch (IOException ex) {
          // report
        } finally {
           try {writer.close();} catch (Exception ex) {/*ignore*/}
        }
    }
    
    // converts JsonList to a string
    public String toString(){
        String str = "{";
        for(int i = 0; i<jsonList.size(); i++){
            str += jsonList.get(i).toString();
            if(i != jsonList.size() - 1){
                str += ", ";
            }                    
        }
        str += "}";
        return str;
    }

    // Adds an jsonWorker to the end of JsonList
    public void addObj(JsonWorker json){
        jsonList.add(json);        
    }
    

    // Removes the JsonWoker at index from JsonList
    public JsonWorker removeObj(int index){
        return jsonList.remove(index);        
    }
    
    public JsonList query(String sql){

		var returnfields = sql.match();
		Matcher m = mPattern.matcher(sql);
		
		var ops = { 
			fields: returnfields[2].replace(' ','').split(','), 
			from: returnfields[3].replace(' ',''), 
			where: (returnfields[4] == undefined)? "true":returnfields[4],
			orderby: (returnfields[5] == undefined)? []:returnfields[5].replace(' ','').split(','),
			order: (returnfields[6] == undefined)? "asc":returnfields[6],
			limit: (returnfields[7] == undefined)? []:returnfields[7].replace(' ','').split(',')
		};

		return this.parse(json, ops);		
	},
	
	public JsonList parse(json,ops){
		var o = { fields:["*"], from:"json", where:"", orderby:[], order: "asc", limit:[] };
		for(i in ops) o[i] = ops[i];

		var result = [];		
		result = this.returnFilter(json,o);
		result = this.returnOrderBy(result,o.orderby,o.order);
		result = this.returnLimit(result,o.limit);
				
		return result;
	},
	
	public JsonList returnFilter(json,jsonsql_o){
		
		var jsonsql_scope = eval(jsonsql_o.from);
		var jsonsql_result = [];
		var jsonsql_rc = 0;

		if(jsonsql_o.where == "") 
			jsonsql_o.where = "true";

		for(var jsonsql_i in jsonsql_scope){
			with(jsonsql_scope[jsonsql_i]){
				if(eval(jsonsql_o.where)){
					jsonsql_result[jsonsql_rc++] = this.returnFields(jsonsql_scope[jsonsql_i],jsonsql_o.fields);
				}
			}
		}
		
		return jsonsql_result;
	},
	
	public JsonList returnFields(scope,fields){
		if(fields.length == 0)
			fields = ["*"];
			
		if(fields[0] == "*")
			return scope;
			
		var returnobj = {};
		for(var i in fields)
			returnobj[fields[i]] = scope[fields[i]];
		
		return returnobj;
	},
	
	public JsonList returnOrderBy(result,orderby,order){
		if(orderby.length == 0) 
			return result;
		
		result.sort(function(a,b){	
			switch(order.toLowerCase()){
				case "desc": return (eval('a.'+ orderby[0] +' < b.'+ orderby[0]))? 1:-1;
				case "asc":  return (eval('a.'+ orderby[0] +' > b.'+ orderby[0]))? 1:-1;
				case "descnum": return (eval('a.'+ orderby[0] +' - b.'+ orderby[0]));
				case "ascnum":  return (eval('b.'+ orderby[0] +' - a.'+ orderby[0]));
			}
		});

		return result;	
	},
	
	public JsonList returnLimit (result,limit){
		switch(limit.length){
			case 0: return result;
			case 1: return result.splice(0,limit[0]);
			case 2: return result.splice(limit[0]-1,limit[1]);
		}
	}
    
    
}
