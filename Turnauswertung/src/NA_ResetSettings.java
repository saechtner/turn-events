import NA_Controller.NA_JSONController;

public class NA_ResetSettings {
    public static void main(String[] args){
        NA_JSONController.resetJSONToDefault(NA_JSONController.settingsPath());
    }
}
