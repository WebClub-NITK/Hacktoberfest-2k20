import 'package:OAuth_login/auth/auth.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:google_sign_in/google_sign_in.dart';

class PhoneVarScreen extends StatefulWidget {
  @override
  _PhoneVarScreenState createState() => _PhoneVarScreenState();
}

GoogleSignIn _googleSignIn = GoogleSignIn();

class _PhoneVarScreenState extends State<PhoneVarScreen> {
  String _verificationId;
  String _phoneNo;
  String _smsCode;
  bool codeSent = false;
  bool whichMethod = false;
  bool isLoading = false;
  bool isSignin = false;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Auth App"),
      ),
      body: AnimatedContainer(
        curve: Curves.bounceOut,
        duration: Duration(milliseconds: 500),
        color: Colors.blue,
        child: Center(
          child: Form(
            child: SafeArea(
              child: Padding(
                padding: EdgeInsets.all(50),
                child: ListView(
                  children: [
                    RaisedButton(
                      padding: EdgeInsets.fromLTRB(30, 10, 30, 10),
                      onPressed: () => _handleSignIn(),
                      color: Colors.deepPurple,
                      child: Center(child: Text("SignIn with Google")),
                    ),
                    SizedBox(
                      height: 30,
                    ),
                    RaisedButton(
                      onPressed: () {
                        setState(() {
                          this.whichMethod = true;
                        });
                      },
                      padding: EdgeInsets.fromLTRB(30, 10, 30, 10),
                      color: Colors.deepPurple,
                      child: Center(child: Text("SignIn with Phone Number")),
                    ),
                    whichMethod
                        ? Padding(
                            padding: const EdgeInsets.all(10.0),
                            child: Column(
                              mainAxisAlignment: MainAxisAlignment.start,
                              children: [
                                TextFormField(
                                    keyboardType: TextInputType.phone,
                                    decoration: InputDecoration(
                                        alignLabelWithHint: true,
                                        // hintText: "795465XXXX",
                                        labelText: "795465XXXX"),
                                    onFieldSubmitted: (value) {
                                      setState(() {
                                        this._phoneNo = value;
                                      });
                                    }),
                                TextFormField(
                                  decoration: InputDecoration(
                                      alignLabelWithHint: true,
                                      // hintText: "795465XXXX",
                                      labelText: "Enter Otp"),
                                  onFieldSubmitted: (value) {
                                    setState(() {
                                      this._smsCode = value;
                                    });
                                  },
                                ),
                                RaisedButton(
                                    color: Colors.deepPurple,
                                    padding:
                                        EdgeInsets.fromLTRB(40, 10, 40, 10),
                                    child: isLoading
                                        ? Text("Login")
                                        : CircleAvatar(),
                                    onPressed: () {
                                      AuthProvider().signInWithOtp(
                                          _smsCode, _verificationId);
                                      setState(() {
                                        isLoading = true;
                                      });
                                    }),
                              ],
                            ),
                          )
                        : Container(),
                  ],
                ),
              ),
            ),
          ),
        ),
      ),
    );
  }

  Future<void> _varifyPhone(String _phoneNo) async {
    final PhoneVerificationCompleted varified = (AuthCredential authResult) {
      AuthProvider().signIn(authResult);
    };
    final PhoneVerificationFailed verificationFailed =
        (FirebaseAuthException authExecption) {
      print("${authExecption.message}");
    };
    final PhoneCodeSent phoneCodeSent = (String verId, [int forceResend]) {
      this._verificationId = verId;
    };
    final PhoneCodeAutoRetrievalTimeout autoRetrievalTimeout = (String verId) {
      this._verificationId = verId;
    };
    await FirebaseAuth.instance.verifyPhoneNumber(
        phoneNumber: _phoneNo,
        timeout: const Duration(seconds: 60),
        verificationCompleted: varified,
        verificationFailed: verificationFailed,
        codeSent: phoneCodeSent,
        codeAutoRetrievalTimeout: autoRetrievalTimeout);
  }

  Future<void> _handleSignIn() async {
    try {
      final isSignin = await _googleSignIn.signIn();
    } catch (error) {
      print(error);
    }
  }
}
