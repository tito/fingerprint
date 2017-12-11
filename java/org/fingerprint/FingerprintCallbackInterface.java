
import android.hardware.fingerprint.FingerprintManager;

public interface FingerprintCallbackInterface {
    public void onAuthenticationError(int errorCode, CharSequence errString);
    public void onAuthenticationFailed();
    public void onAuthenticationHelp(int helpCode, CharSequence helpString);
    public void onAuthenticationSucceeded(FingerprintManager.AuthenticationResult result);
}
