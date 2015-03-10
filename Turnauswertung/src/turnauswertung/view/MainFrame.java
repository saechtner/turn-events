package turnauswertung.view;


import javax.swing.*;

import turnauswertung.controller.JSONController;


import java.awt.*;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

public class MainFrame extends JFrame{

    /**  */
	private static final long serialVersionUID = 1L;
	
	JPanel content;

    public MainFrame(){
        super("Turnwettkampf - Auswertung (alpha)");

        content = new JPanel();
        content.add(new JLabel("Much to do here!"));

        setContentPane(content);
        addMenu();

        initializeProperties();
    }

    private void initializeProperties() {
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(JSONController.getWindowExtent());
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
                JSONController.setWindowExtent(getSize());
            }
        });
    }
}
