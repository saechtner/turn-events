package NA_View;

import javax.swing.*;

public class NA_MainView extends JFrame{

    JPanel content;

    public NA_MainView(){
        super("Turnwettkampf - Auswertung (alpha)");

        content = new JPanel();

        setContentPane(content);

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setExtendedState(JFrame.MAXIMIZED_BOTH);
        setVisible(true);
        setResizable(false);

    }
}
