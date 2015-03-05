import NA_Controller.JSONController;

public class ResetSettings {
    public static void main(String[] args){
        JSONController.resetJSONToDefault(JSONController.settingsPath());
    }
}
