package Model.Database_Connection;

import java.sql.DriverManager;
import java.util.List;

public class MySQL_Connector extends DB_Connector {
    protected String username;
    protected String userPassword;
    protected String url;

    protected String getUsername() {
        return username;
    }

    protected void setUsername(String newUsername) {
        this.username = newUsername;
    }

    protected String getUserPassword() {
        return userPassword;
    }

    protected void setUserPassword(String newUserPassword) {
        this.userPassword = newUserPassword;
    }

    protected String getUrl() {
        return url;
    }

    protected void setUrl(String newUrl) {
        this.url = newUrl;
    }

    public MySQL_Connector(String databaseName, String url, String username, String userPassword){
        setDatabaseName(databaseName);
        setUrl(url);
        setUsername(username);
        setUserPassword(userPassword);
    }

    public MySQL_Connector(String databaseName, String username, String userPassword){
        setDatabaseName(databaseName);
        setUrl("localhost:3306/");
        setUsername(username);
        setUserPassword(userPassword);
    }

    protected void connect() {
        try {
            setConnection(DriverManager.getConnection(
                    urlPrefix()+getUrl()+getDatabaseName(),
                    getUsername(),
                    getUserPassword()));
        } catch(Exception e){
            e.printStackTrace();
        }
    }

    public void executeQuery(String query) {
        connect();


        disconnect();
    }

    public List<String> retrieveData(String query) {
        connect();


        disconnect();
        return null;
    }

    // Constants
    protected String urlPrefix(){
        return super.urlPrefix()+"sql://";
    }
}