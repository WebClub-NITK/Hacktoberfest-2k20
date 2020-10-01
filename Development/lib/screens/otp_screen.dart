import 'package:flutter/material.dart';

class OtpScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    var _otp;
    return Container(
      child: Center(
          child: Container(
              child: Column(
        children: [
          TextField(
            controller: _otp,
            autofocus: true,
            decoration: InputDecoration(
              labelText: "Enter OTP",
            ),
          ),
          GestureDetector(
            child: AnimatedContainer(
              duration: null,
              child: Center(
                child: Text("Varify"),
              ),
            ),
          )
        ],
      ))),
    );
  }
}
