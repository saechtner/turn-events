package turnauswertung;
import turnauswertung.controller.JSONController;

public class ResetSettings {
	
    public static void main(String[] args){
        JSONController.resetJSONToDefault(JSONController.settingsPath());
    }
}
