package General;
import agentes.AgenteBase;
import agentes.AgenteBasePadre;
import agentes.AgenteHijo;
import jade.core.Profile;
import jade.core.ProfileImpl;
import jade.wrapper.AgentContainer;
import jade.wrapper.AgentController;
import jade.wrapper.StaleProxyException;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Contenedor {
    AgentController agent;
    AgentContainer container;

    public void crearContenedor() {
        jade.core.Runtime runtime = jade.core.Runtime.instance();
        Profile profile = new ProfileImpl(null, 1090, null);
        container = runtime.createMainContainer(profile);
        agregarAgentes();

    }
    private void agregarAgentes() {
        try {
            container.createNewAgent("AgenteBasePadre",
                    AgenteBasePadre.class.getName(), new Object[] {this}).start();
            container.createNewAgent("AgenteBase",
                    AgenteBase.class.getName(),
                    null).start();



        } catch (StaleProxyException ex) {
            Logger.getLogger(Contenedor.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
    public void crearHijo(String alias, Object[] info){
        try {
            container.createNewAgent(alias, AgenteHijo.class.getName(), info).start();
        } catch (StaleProxyException ex) {
            Logger.getLogger(Contenedor.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
