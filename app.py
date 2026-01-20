import gradio as gr

custom_css = """
body {
    background: radial-gradient(circle at top, #0b1026, #02040f);
    color: #e0e7ff;
    font-family: 'Segoe UI', sans-serif;
}
.gradio-container {
    max-width: 1100px !important;
}
h1, h2, h3 {
    color: #9fb5ff;
    text-align: center;
}
.section {
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 14px;
    padding: 20px;
    margin-bottom: 20px;
    background: linear-gradient(145deg, rgba(255,255,255,0.06), rgba(255,255,255,0.02));
}
.output-box {
    font-size: 18px;
}
"""

with gr.Blocks(css=custom_css) as demo:

    gr.Markdown("""
    # 🛰️ Satellite Telemetry Intelligence Dashboard  
    ### Alert Probability & Health Score Prediction System  
    _ISRO MCF–Aligned Predictive Analytics Model_
    """)

    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### Communication Metrics")
            signal_strength = gr.Number(label="Signal Strength (dB)")
            uplink_latency = gr.Number(label="Uplink Latency (ms)")
            downlink_latency = gr.Number(label="Downlink Latency (ms)")
            packet_loss = gr.Number(label="Packet Loss (%)")

        with gr.Column(scale=1):
            gr.Markdown("### Power & Thermal Metrics")
            battery_voltage = gr.Number(label="Battery Voltage (V)")
            solar_eff = gr.Number(label="Solar Panel Efficiency (%)")
            temperature = gr.Number(label="Temperature (°C)")
            radiation = gr.Number(label="Radiation Level")

        with gr.Column(scale=1):
            gr.Markdown("### System Load Metrics")
            cpu = gr.Number(label="CPU Load (%)")
            memory = gr.Number(label="Memory Usage (%)")
            error_rate = gr.Number(label="Error Rate (%)")

    gr.Markdown("---")

    predict_btn = gr.Button("Run Prediction", variant="primary")

    output = gr.JSON(label="Prediction Results", elem_classes="output-box")

    predict_btn.click(
        fn=predict_from_input,
        inputs=[
            signal_strength,
            battery_voltage,
            temperature,
            cpu,
            memory,
            uplink_latency,
            downlink_latency,
            packet_loss,
            radiation,
            solar_eff,
            error_rate
        ],
        outputs=output
    )

    gr.Markdown("""
    ---
    🌌 **Designed for Aerospace Predictive Systems**  
    *Telemetry-driven intelligence • Early anomaly detection • Mission readiness*
    """)

demo.launch(share=True)
