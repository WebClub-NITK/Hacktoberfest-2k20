package com.example.bmi;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    EditText height,weight;
    TextView result;
    float bmi;
    public void click(View view){
        String res ="Please enter a valid values";
        float tall=Float.parseFloat(height.getText().toString());
        float mass=Float.parseFloat(weight.getText().toString());
        bmi=mass/(tall*tall);
        if(bmi<18.50){
            res="Underweight";
        }
        else if(bmi>18.50&&bmi<24.99){
            res="Normal range";
        }
        else if(bmi>=25.00) {
            res="Overweight";
        }
        result.setText(res);

    }
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        height=findViewById(R.id.height);
        weight=findViewById(R.id.weight);
        result=findViewById(R.id.result);
    }
}