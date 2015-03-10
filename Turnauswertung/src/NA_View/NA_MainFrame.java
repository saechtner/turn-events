package NA_View;

import NA_Controller.NA_JSONController;

import javax.swing.*;
import java.awt.*;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

public class NA_MainFrame extends JFrame{

    JPanel content;

    public NA_MainFrame(){
        super("Turnwettkampf - Auswertung (alpha)");

        content = new JPanel();
        content.add(new JLabel("Much to do here!"));

        setContentPane(content);
        addMenu();

        initializeProperties();
    }

    private void initializeProperties() {
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(NA_JSONController.getWindowExtent());
        setVisible(true);
        setMinimumSize(new Dimension(320,240));
        getContentPane().setBackground(new Color(127, 127, 127));
        savePropertiesOnClose();
    }


    private void addMenu(){
        JMenuBar menuBar = new JMenuBar();
        menuBar.add(new JMenuItem("Test"));

        setJMenuBar(menuBar);
    }

    private void savePropertiesOnClose() {
        addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e) {
                NA_JSONController.setWindowExtent(getSize());
            }
        });
    }
}
