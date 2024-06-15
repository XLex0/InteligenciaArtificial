package General;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.io.IOException;

public class Conexion {

    public static String ejecutar(int a, int b) {
        String scriptPath = "src/python/entrada.py";
        String cmd = "python " + scriptPath;
        try {
            Process p = Runtime.getRuntime().exec(cmd);

            PrintWriter writer = new PrintWriter(new OutputStreamWriter(p.getOutputStream()));
            writer.println(a);  // Supongamos que el usuario ingresa 3 para 'a'
            writer.println(b);  // Supongamos que el usuario ingresa 5 para 'b'
            writer.flush();
            writer.close();

            // Leer la salida del proceso
            BufferedReader reader = new BufferedReader(new InputStreamReader(p.getInputStream()));
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println("Salida: " + line);
                return line;
            }
            reader.close();

            // Leer los errores del proceso
            BufferedReader errorReader = new BufferedReader(new InputStreamReader(p.getErrorStream()));
            while ((line = errorReader.readLine()) != null) {
                System.err.println("Error: " + line);
            }
            errorReader.close();

            // Esperar a que el proceso termine y obtener el código de salida
            int exitCode = p.waitFor();
            System.out.println("Código de salida: " + exitCode);

        }catch (Exception e){
            e.printStackTrace();
        }
        return "";
    }

}
