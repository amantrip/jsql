/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package jsonworker;
import org.json.simple.JSONObject;//.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.Writer;

import java.util.*;
/**
 *
 * @author Seth
 */
public class JsonWorker {
    
    public JSONObject thisObj; 
    
    public JsonWorker(){
        thisObj = new JSONObject();    
    }
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
        
    public void writeToFile(String fileName){
        Writer writer = null;

        try {
            writer = new BufferedWriter(new OutputStreamWriter(
                  new FileOutputStream(fileName), "utf-8"));
            writer.write(this.toString());
        } catch (IOException ex) {
        } finally {
           try {writer.close();} catch (Exception ex)
        }
    }

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
    
    public String toString(){
        return thisObj.toString();
    }
    
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
    
    public JSONObject subtractor(JSONObject obj){
        JSONObject diffJSON = new JSONObject();
        for(Iterator iterator = thisObj.keySet().iterator(); iterator.hasNext();){
            Object key = iterator.next();
            if(obj.get(key) != null){
                // this if statement works for primiative type
                // need to expand for objects
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
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args)  {
        // TODO code application logic here
        
    }
    
}
