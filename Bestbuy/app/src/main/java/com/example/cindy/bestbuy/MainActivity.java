package com.example.cindy.bestbuy;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    Button Helpbutton,Locationbutton;
    RadioGroup radioGroup;
    RadioButton ParkRoyal, Downtown, Richmond;
    String selectedLocation;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        initialize();

    }



    @Override
    public void onClick(View v) {
        switch (v.getId()) {

            case R.id.button2:
                //

                break;
            case R.id.button:
                if (ParkRoyal.isChecked()) {
                    selectedLocation = ParkRoyal.getText().toString();
                } else if (Downtown.isChecked()) {
                    selectedLocation = Downtown.getText().toString();
                } else if (Richmond.isChecked()) {
                    selectedLocation = Richmond.getText().toString();
                }
                Toast.makeText(getApplicationContext(), selectedLocation, Toast.LENGTH_LONG).show();
                break;
        }
    }


    public void initialize(){

            Helpbutton = (Button) findViewById(R.id.button2);
            Helpbutton.setOnClickListener(this);
            Locationbutton = (Button) findViewById(R.id.button);
            Locationbutton.setOnClickListener(this);
            radioGroup = (RadioGroup) findViewById(R.id.myRadioGroup);
            ParkRoyal = (RadioButton) findViewById(R.id.radioButton4);
            Downtown = (RadioButton) findViewById(R.id.radioButton5);
            Richmond = (RadioButton) findViewById(R.id.radioButton6);

    }





}
