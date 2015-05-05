/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
//package jsonworker;
import org.json.simple.JSONObject;//.JSONObject;
import java.util.*;
/**
 *
 * @author Seth
 */
public class JsonWorker {
    

    // Do we want to keep the objects untouched or modified ? 
    public static JSONObject adder(JSONObject obj1, JSONObject obj2){
        JSONObject sum = new JSONObject();
        for(Iterator iterator = obj1.keySet().iterator(); iterator.hasNext();) {
            Object key = iterator.next();
            sum.put(key, obj1.get(key));
        }
        
        for(Iterator iterator = obj2.keySet().iterator(); iterator.hasNext();) {
            Object key = iterator.next();
            if(obj1.get(key) == null){
                sum.put(key, obj2.get(key));
            }
        }
        return sum;
    }
    
    public static JSONObject subtractor(JSONObject obj1, JSONObject obj2){
        JSONObject diffJSON = new JSONObject();
        for(Iterator iterator = obj1.keySet().iterator(); iterator.hasNext();){
            Object key = iterator.next();
            if(obj2.get(key) != null){
                // this if statement works for primiative type
                // need to expand for objects
                if(obj1.get(key) != obj2.get(key)){
                    diffJSON.put(key, obj1.get(key));                
                }
            }
            else{
                diffJSON.put(key, obj1.get(key));
            }
        }
        return diffJSON;
    }

    public static JSONObject intersect(JSONObject obj1, JSONObject obj2){
        JSONObject intersectionJSON = new JSONObject();
        for(Iterator iterator = obj1.keySet().iterator(); iterator.hasNext();) {
            Object key = iterator.next();
            if(obj1.get(key) == obj2.get(key)){
                intersectionJSON.put(key, obj1.get(key));
            }
        }
        
        return intersectionJSON;

    }
    public static JSONObject union(JSONObject obj1, JSONObject obj2){
        JSONObject unionJSON = adder(obj1,obj2);
 
        for(Iterator iterator = obj1.keySet().iterator(); iterator.hasNext();) {
            Object key = iterator.next();
            if(obj2.get(key) != null){
                if(obj1.get(key) == obj2.get(key)){
                    unionJSON.put(key,obj1.get(key));
                }
                else{
                    Object[] union = {obj1.get(key), obj2.get(key)};
                    unionJSON.put(key,union);
                }
            }
            else{
                unionJSON.put(key, obj1.get(key));
            }
        }
        for(Iterator iterator = obj2.keySet().iterator(); iterator.hasNext();) {
            Object key = iterator.next();
            if(unionJSON.get(key) == null){
                unionJSON.put(key,obj2.get(key));
            }
        }
        return unionJSON;

    }
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        String jsonString = "";
        JSONObject test = new JSONObject();
        test.put("a", "a");
        test.put("b", "b");
        test.put("c", "c");
        test.put("d", "d");
        JSONObject test2 = new JSONObject();
        test2.put("a", "a");
        test2.put("b", "b");
        test2.put("d", "c");
        test2.put("d", "e");
        System.out.println(subtractor(test2, test));
        System.out.println(subtractor(test, test2));
        System.out.println(adder(test2, test));  
        System.out.println(intersect(test2, test));  
        System.out.println(test2);          
    }
    
}
