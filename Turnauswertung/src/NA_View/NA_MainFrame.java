package NA_View;

import javax.swing.*;
import java.awt.*;

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
        setExtendedState(JFrame.MAXIMIZED_BOTH);
        setVisible(true);
        setResizable(false);
        getContentPane().setBackground(new Color(127, 127, 127));
    }


    private void createMenu(){
        JMenuBar menuBar = new JMenuBar();
        menuBar.add(new JMenuItem("Test"));

        setJMenuBar(menuBar);
    }

}
