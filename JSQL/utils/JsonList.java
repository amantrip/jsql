
import jsonworker.JsonWorker;
import java.util.ArrayList;
import org.json.simple.JSONObject;
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Seth
 */
public class JsonList {

    ArrayList<JsonWorker> jsonList = new ArrayList<JsonWorker>();

    
    public JsonList(JsonWorker[] list){
        for(int i = 0; i<list.length; i++){
            jsonList.add(list[i]);
        }
    }

    public void addObj(JsonWorker json){
        jsonList.add(json);        
    }
    
    public JsonWorker removeObj(int index){
        return jsonList.remove(index);        
    }
    
    
}
