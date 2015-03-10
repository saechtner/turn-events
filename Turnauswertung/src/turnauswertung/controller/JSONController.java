package turnauswertung.controller;

import com.google.gson.GsonBuilder;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

import java.awt.*;
import java.io.FileReader;
import java.io.FileWriter;


public class JSONController {

    private static JSONParser jsonParser = new JSONParser();

    public static JSONParser jsonParser(){
        return jsonParser;
    }

    public static String settingsPath(){
        return "src/Model/JSON/settings.json";
    }

    public static String statsPath(){
        return "src/Model/JSON/stats.json";
    }

    private static JSONObject getJSONObject(String path){
        try {
            return (JSONObject) jsonParser().parse(new FileReader(path));
        } catch(Exception e){
            System.out.println("Version: "+getVersion());
            System.out.println("Input: "+path);
            e.printStackTrace();
            return null;
        }
    }

    private static void writeJSONObject(String path, JSONObject jsonObject){
        try {
            FileWriter file = new FileWriter(path);
            file.write(new GsonBuilder().setPrettyPrinting().create().toJson(jsonObject));
            file.flush();
            file.close();
        } catch(Exception e){
            System.out.println("Version: "+getVersion());
            System.out.println("Input: "+path);
            e.printStackTrace();
        }
    }

    public static void basicSetter(String path, String key, int value){
        JSONObject jsonObject = getJSONObject(path);
        jsonObject.put(key, value);
        writeJSONObject(path, jsonObject);
    }

    public static void basicSetter(String path, String key, double value){
        JSONObject jsonObject = getJSONObject(path);
        jsonObject.put(key, value);
        writeJSONObject(path, jsonObject);
    }

    public static void basicSetter(String path, String key, String value){
        JSONObject jsonObject = getJSONObject(path);
        jsonObject.put(key, value);
        writeJSONObject(path, jsonObject);
    }

    public static int getWindowWidth(){
        return ((Long) getJSONObject(settingsPath()).get("windowWidth")).intValue();
    }

    public static void setWindowWidth(int width){
        basicSetter(settingsPath(), "windowWidth", width);

    }

    public static int getWindowHeight(){
        return ((Long) getJSONObject(settingsPath()).get("windowHeight")).intValue();
    }

    public static void setWindowHeight(int height){
        basicSetter(settingsPath(), "windowHeight", height);
    }

    public static Dimension getWindowExtent(){
        return new Dimension(getWindowWidth(), getWindowHeight());
    }

    public static void setWindowExtent(Dimension dimension){
        setWindowWidth(dimension.width);
        setWindowHeight(dimension.height);
    }

    public static void setWindowExtent(int width, int height){
        setWindowWidth(width);
        setWindowHeight(height);
    }

    public static String getVersion(){
            return (String) getJSONObject(statsPath()).get("version");
    }

    public static void resetJSONToDefault(String path){
        JSONObject initialJSONObject = getJSONObject("initial_"+path);
        writeJSONObject(path, initialJSONObject);
    }
}
