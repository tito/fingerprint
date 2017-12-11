import org.fingerprint.FingerprintCallbackInterface;
import android.hardware.fingerprint.FingerprintManager;


public class FingerprintCallback extends FingerprintManager.AuthenticationCallback {

    FingerprintCallbackInterface dispatcher = null;

    public void onAuthenticationError(int errorCode, CharSequence errString) {
        this.dispatcher.onAuthenticationError(errorCode, errString);
    }

    public void onAuthenticationFailed() {
        this.dispatcher.onAuthenticationFailed();
    }

    public void onAuthenticationHelp(int helpCode, CharSequence helpString) {
        this.dispatcher.onAuthenticationHelp(helpCode, helpString);
    }

    public void onAuthenticationSucceeded(FingerprintManager.AuthenticationResult result) {
        this.dispatcher.onAuthenticationSucceeded(result);
    }

    public void setDispatcher(FingerprintCallbackInterface dispatcher) {
        this.dispatcher = dispatcher;
    }

}
