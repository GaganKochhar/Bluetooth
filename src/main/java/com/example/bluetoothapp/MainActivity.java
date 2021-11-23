package com.example.bluetoothapp;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import java.util.Set;

public class MainActivity extends AppCompatActivity {

    private final int REQUEST_ENABLE_BLUETOOTH = 0;
    private final int REQUEST_DISCOVERABLE_BLUETOOTH=1;


    TextView pairedDevices,statusBluetooth;
    Button onBtn,offBtn,discoverableBtn,pairedBtn;
    ImageView bluetoothIc;

    BluetoothAdapter adapter;
    String msg;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        pairedDevices   = findViewById(R.id.pairedDevices);
        statusBluetooth = findViewById(R.id.statusBluetooth);
        onBtn           = findViewById(R.id.onBtn);
        offBtn          = findViewById(R.id.offBtn);
        discoverableBtn = findViewById(R.id.discoverableBtn);
        pairedBtn       = findViewById(R.id.pairedBtn);
        bluetoothIc     = findViewById(R.id.bluetoothIc);

        //setting bluetooth adapter
        adapter=BluetoothAdapter.getDefaultAdapter();

        if(adapter==null){
                statusBluetooth.setText("Bluetooth is not available");
        }
        else{
                statusBluetooth.setText("Bluetooth is available");
        }

        if(adapter.isEnabled()){
            bluetoothIc.setImageResource(R.drawable.ic_bluetooth_on);
        }
        else{
            bluetoothIc.setImageResource(R.drawable.ic_bluetooth_off);
        }
        
        onBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(!adapter.isEnabled()){

                    showToast("Turning On Bluetooth");
                    Intent intent= new Intent(BluetoothAdapter.ACTION_REQUEST_ENABLE);
                    startActivityForResult(intent,REQUEST_ENABLE_BLUETOOTH);

                }
                else{
                    showToast("Bluetooth is already On");
                }
            }
        });
        
        offBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(adapter.isEnabled()){
                    adapter.disable();
                    showToast("Turning off Bluetooth");
                    bluetoothIc.setImageResource(R.drawable.ic_bluetooth_off);
                }
                else{
                    showToast("Bluetooth is already off");
                }
                
            }
        });
        
        discoverableBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(!adapter.isDiscovering()){
                    showToast("Making device Discovering");
                    Intent intent=new Intent(BluetoothAdapter.ACTION_REQUEST_DISCOVERABLE);
                    startActivityForResult(intent,REQUEST_DISCOVERABLE_BLUETOOTH);
                }
                
            }
        });
        
        pairedBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (adapter.isEnabled()) {
                    pairedDevices.setText("Paired Devices ");
                    Set<BluetoothDevice> devices = adapter.getBondedDevices();
                    for (BluetoothDevice device : devices) {
                        pairedDevices.append("\nDevices " + device.getName());
                    }
                }
                else {
                    showToast("Turn on Bluetooth");
                }
            }
        });


    }

    private void showToast(String msg){
        
        Toast.makeText(this, msg, Toast.LENGTH_SHORT).show();
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        switch(requestCode){
            case REQUEST_ENABLE_BLUETOOTH:
                if(resultCode==RESULT_OK){
                    showToast("Bluetooth is on");
                    bluetoothIc.setImageResource(R.drawable.ic_bluetooth_on);
                }
                else{
                    showToast("Bluetooth cannot be switched on");

                }
                break;

        }
        super.onActivityResult(requestCode, resultCode, data);

    }
}


