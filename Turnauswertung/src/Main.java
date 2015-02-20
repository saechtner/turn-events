import NA_Model.NA_Database_Connection.NA_DB_Connector;
import NA_View.NA_MainView;

public class Main {

    public static void main(String[] args) {

        // test
        NA_DB_Connector con = new NA_DB_Connector("","","");

        NA_MainView window = new NA_MainView();
    }
}
