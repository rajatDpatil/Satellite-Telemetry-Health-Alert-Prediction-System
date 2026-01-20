def predict_from_input(
    signal_strength,
    battery_voltage,
    temperature,
    cpu_load,
    memory_usage,
    uplink_latency,
    downlink_latency,
    packet_loss,
    radiation_level,
    solar_panel_efficiency,
    error_rate
):
    import pandas as pd

    input_df = pd.DataFrame([[
        signal_strength,
        battery_voltage,
        temperature,
        cpu_load,
        memory_usage,
        uplink_latency,
        downlink_latency,
        packet_loss,
        radiation_level,
        solar_panel_efficiency,
        error_rate
    ]], columns=X.columns)

  
    input_scaled = scaler.transform(input_df)

    alert_prob = alert_model.predict_proba(input_scaled)[0][1]
    health_pred = health_model.predict(input_scaled)[0]

    if alert_prob < 0.2 and health_pred >= 40:
        status = "NORMAL"
    elif alert_prob < 0.6:
        status = "WARNING"
    else:
        status = "CRITICAL"

    return {
        "Alert Probability": round(alert_prob, 2),
        "Predicted Health Score": round(health_pred, 1),
        "Satellite Status": status
    }
