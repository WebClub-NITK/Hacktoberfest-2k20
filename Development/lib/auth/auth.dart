import 'package:OAuth_login/main.dart';
import 'package:OAuth_login/screens/authscreen.dart';
import 'package:OAuth_login/screens/phoneVarScreen.dart';
import 'package:OAuth_login/screens/splashScreen.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:google_sign_in/google_sign_in.dart';

GoogleSignIn _googleSignIn = GoogleSignIn(signInOption: SignInOption.standard);

class AuthProvider {
  handleIsAuth() {
    return StreamBuilder(
      stream: FirebaseAuth.instance.authStateChanges(),
      builder: (BuildContext context, snapshot) {
        if (snapshot.hasData) {
          return MyHomePage();
        } else {
          return SplashScreen();
        }
      },
    );
  }

  Future<void> signOut() async {
    await _googleSignIn.disconnect();
    FirebaseAuth.instance.signOut();
  }

  signIn(AuthCredential authCredential) {
    FirebaseAuth.instance.signInWithCredential(authCredential);
  }

  signInWithOtp(smsCode, verId) {
    AuthCredential authCredential =
        PhoneAuthProvider.credential(verificationId: verId, smsCode: smsCode);
    signIn(authCredential);
  }
}
