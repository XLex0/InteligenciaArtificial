package General;
import jade.core.AID;
import jade.core.Agent;
import jade.domain.FIPANames;
import jade.lang.acl.ACLMessage;
import java.io.IOException;
import java.io.Serializable;
import java.util.logging.Level;
import java.util.logging.Logger;
public class Msj {

    public static void sendMSJ(int tipo, String receptor, Agent emisor,
                               String codigoConversationId,
                               String contenidoString, Serializable contenidoObject,
                               boolean isContentString){
        ACLMessage acl = new ACLMessage(tipo);
        AID id = new AID();
        id.setLocalName(receptor);
        acl.addReceiver(id);
        acl.setSender(emisor.getAID());
        acl.setLanguage(FIPANames.ContentLanguage.FIPA_SL);
        acl.setConversationId(codigoConversationId);
        if (isContentString){
            acl.setContent(contenidoString);

        }else{
            try {
                acl.setContentObject(contenidoObject);
            } catch (IOException ex) {
                Logger.getLogger(Msj.class.getName()).log(Level.SEVERE, null, ex);
            }
        }
        emisor.send(acl);

    }
}
