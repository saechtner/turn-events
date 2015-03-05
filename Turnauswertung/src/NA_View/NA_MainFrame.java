package NA_View;

import NA_Controller.JSONController;
import org.json.simple.JSONObject;

import javax.swing.*;
import java.awt.*;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.io.FileReader;
import java.io.IOException;

public class NA_MainFrame extends JFrame{

    JPanel content;

    public NA_MainFrame(){
        super("Turnwettkampf - Auswertung (alpha)");

        content = new JPanel();
        content.add(new JLabel("Much to do here!"));

        setContentPane(content);

        initializeProperties();
        createMenu();
    }

    private void initializeProperties() {
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
//        setExtendedState(JFrame.MAXIMIZED_BOTH);
        setSize(JSONController.getWindowExtent());
        setVisible(true);
        setMinimumSize(new Dimension(320,240));
//        setResizable(false);
        getContentPane().setBackground(new Color(127, 127, 127));
        savePropertiesOnClose();
    }


    private void createMenu(){
        JMenuBar menuBar = new JMenuBar();
        menuBar.add(new JMenuItem("Test"));

        setJMenuBar(menuBar);
    }

    private void savePropertiesOnClose() {
        addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e) {
                JSONController.setWindowExtent(getSize());
            }
        });
    }
}
