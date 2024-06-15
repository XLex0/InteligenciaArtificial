package General;
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
public class GUI extends JFrame  implements ActionListener {
    private final JTextField textField1, textField2, textField3;
    private final JButton ingresarButton;
    private int text1;
    private int text2;

    public GUI(){

        setTitle("IA");
        setSize(800, 450);
        setDefaultCloseOperation(EXIT_ON_CLOSE);

        // Crear paneles
        JPanel panel = new JPanel();
        panel.setLayout(new GridLayout(4, 1));

        // Crear componentes
        JLabel label1 = new JLabel("Campo 1:");
        JLabel label2 = new JLabel("Campo 2:");
        JLabel label3 = new JLabel("resultado:");
        textField1 = new JTextField(5);
        textField2 = new JTextField(5);
        textField3 = new JTextField(5);
        textField3.setEditable(false);
        ingresarButton = new JButton("Ingresar");

        // Agregar componentes al panel
        panel.add(label1);
        panel.add(textField1);
        panel.add(label2);
        panel.add(textField2);
        panel.add(label3);
        panel.add(textField3);
        panel.add(ingresarButton);

        // Agregar panel al marco
        add(panel);

        // Escuchar eventos del botón
        ingresarButton.addActionListener(this);

        // Mostrar la ventana
        setVisible(true);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == ingresarButton) {
            boolean bandera = false;

                try {
                    text1 =Integer.parseInt(textField1.getText());
                    text2 =Integer.parseInt(textField2.getText());
                    bandera = true;
                }catch (Exception a) {
                    System.out.println("No valido");
                }
                if (bandera) {
                    System.out.println("Texto ingresado en Campo 1: " + text1);
                    System.out.println("Texto ingresado en Campo 2: " + text2);
                    String resultado = Conexion.ejecutar(text1, text2);
                    textField3.setText(String.valueOf(resultado));
                }

        }
    }



}

