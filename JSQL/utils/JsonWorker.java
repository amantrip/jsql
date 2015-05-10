package jsonworker;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.Writer;
import org.json.simple.JSONObject;//.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

import java.util.*;


// Each instance of JsonWorker is a json object in our language
public class JsonWorker {
    
    // the json object with which we mold to resemble our langauge's json object
    public JSONObject thisObj; 
    
    // empty constructor creates empty json object
    public JsonWorker(){
        thisObj = new JSONObject();    
    }

    // creates json object based on a parsed string.
    // throws exception if string cannot be parsed
    public JsonWorker(String s) throws ParseException{
        JSONParser parser = new JSONParser();    
        try{
            thisObj = (JSONObject)parser.parse(s);
            
        }catch(ParseException pe){
         System.out.println("position: " + pe.getPosition());
         System.out.println(pe);
         throw pe;
        }   
    }

    // converts thisObj to a string and writes it to fileName
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

    // parses the text in fileName and returns the equivalent json object 
    public JsonWorker readFile(String fileName) throws FileNotFoundException, IOException, ParseException{
        String everything;
        BufferedReader br = new BufferedReader(new FileReader(fileName));
         try {
             StringBuilder sb = new StringBuilder();
             String line = br.readLine();

             while (line != null) {
                 sb.append(line);
                 sb.append(System.lineSeparator());
                 line = br.readLine();
             }
             everything = sb.toString();
         } finally {
             br.close();
         }
         return new JsonWorker(everything);
    }
    
    // converts thisObj to a string
    public String toString(){
        return thisObj.toString();
    }
    
    // returns a json object that contains the entirety of thisObj as well as 
    // the fields (and associated values) that obj has that thisObj does not
    public JSONObject adder(JSONObject obj){
        JSONObject sum = new JSONObject();
        for(Iterator iterator = thisObj.keySet().iterator(); iterator.hasNext();) {
            Object key = iterator.next();
            sum.put(key, thisObj.get(key));
        }
        
        for(Iterator iterator = obj.keySet().iterator(); iterator.hasNext();) {
            Object key = iterator.next();
            if(thisObj.get(key) == null){
                sum.put(key, obj.get(key));
            }
        }
        return sum;
    }

    // returns a json object containing thisObj's data less any key/values pairs
    // it shares with obj
    public JSONObject subtractor(JSONObject obj){
        JSONObject diffJSON = new JSONObject();
        for(Iterator iterator = thisObj.keySet().iterator(); iterator.hasNext();){
            Object key = iterator.next();
            if(obj.get(key) != null){
                if(thisObj.get(key) != obj.get(key)){
                    diffJSON.put(key, thisObj.get(key));                
                }
            }
            else{
                diffJSON.put(key, thisObj.get(key));
            }
        }
        return diffJSON;
    }

    // returns a json that returns the overlap in key/values pairs 
    // of thisObj and obj
    public JSONObject intersect(JSONObject obj){
        JSONObject intersectionJSON = new JSONObject();
        for(Iterator iterator = thisObj.keySet().iterator(); iterator.hasNext();) {
            Object key = iterator.next();
            if(thisObj.get(key) == obj.get(key)){
                intersectionJSON.put(key, thisObj.get(key));
            }
        }
        
        return intersectionJSON;

    }
    
    // returns a json that contains a merge of both thisObj and obj such that
    // all disjoint fields and their assocaited values are included as is. 
    // any field that thisObj and obj share in common is added to the json 
    // where the value is an array containing the values of the field 
    // from thisObj and obj (where thisObj's value is the 0th index)
    public JSONObject union(JSONObject obj){
        JSONObject unionJSON = this.adder(obj); 
        for(Iterator iterator = thisObj.keySet().iterator(); iterator.hasNext();) {
            Object key = iterator.next();
            if(obj.get(key) != null){
                if(thisObj.get(key) == obj.get(key)){
                    unionJSON.put(key,thisObj.get(key));
                }
                else{
                    Object[] union = {thisObj.get(key), obj.get(key)};
                    unionJSON.put(key,union);
                }
            }
            else{
                unionJSON.put(key, thisObj.get(key));
            }
        }
        for(Iterator iterator = obj.keySet().iterator(); iterator.hasNext();) {
            Object key = iterator.next();
            if(unionJSON.get(key) == null){
                unionJSON.put(key,obj.get(key));
            }
        }
        return unionJSON;

    }

    public static void main(String[] args)  {
        return;
    }
}