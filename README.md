# 🛰️ Satellite Telemetry Health & Alert Prediction System

## Brief Summary
An ISRO MCF-aligned machine learning project that analyzes satellite telemetry data to predict **Alert Probability** and **Satellite Health Score**, enabling early anomaly detection and informed operational decision-making through a real-time dashboard.


## Overview
Satellite operations rely on continuous telemetry monitoring to ensure mission safety and reliability. This project simulates a **ground-station analytics system** similar to those used at **ISRO Master Control Facility (MCF)**, applying machine learning to interpret raw telemetry signals and assess satellite health in real time.

The system processes telemetry data from multiple subsystems including communication, power, thermal, and system load metrics, providing mission operators with actionable insights for proactive decision-making.


## Problem Statement
Manual or threshold-based monitoring of satellite telemetry can miss early warning patterns and does not scale well with increasing data volume. There is a need for a **predictive, data-driven system** that can proactively identify risk conditions and summarize overall satellite health before critical failures occur.


## Tools and Technologies
- **Programming Language:** Python  
- **Machine Learning:** Scikit-learn  
- **Data Processing:** Pandas, NumPy  
- **Visualization & UI:** Gradio  
- **Environment:** Google Colab  


## Methods
The system follows a comprehensive machine learning pipeline:

1. **Data Generation:** Generated realistic, raw satellite telemetry data reflecting communication, power, thermal, and system load conditions
2. **Preprocessing:** Applied data preprocessing and feature scaling to handle noisy and unstructured inputs
3. **Model Development:** Built dual predictive models:
   - A **classification model** to predict Alert Probability  
   - A **regression model** to estimate Satellite Health Score
4. **Decision Logic:** Implemented rule-based logic to categorize satellite status as **NORMAL, WARNING, or CRITICAL**
5. **Deployment:** Created a real-time interactive dashboard using Gradio for operational use


## Key Insights
- Combined telemetry parameters provide stronger predictive signals than isolated metrics
- Feature scaling is critical for consistent and stable predictions across different telemetry ranges
- Dual-model architecture (classification + regression) improves interpretability for mission operators
- Anomaly-aware decision logic enables mission-critical reliability in operational scenarios


## Dashboard Output
The Gradio dashboard allows users to:
- Enter live telemetry values for real-time analysis
- View Alert Probability and Health Score instantly
- Understand satellite status through clear categorical output (NORMAL/WARNING/CRITICAL)
- Support decision-making with intuitive visualizations and metrics


## Results & Conclusion
- Successfully predicted satellite health trends and alert risks from raw telemetry data
- Demonstrated the effectiveness of machine learning for **proactive satellite monitoring**
- The system closely aligns with **ISRO MCF-style telemetry analysis workflows** and supports early anomaly detection
- Provides a scalable foundation for real-world satellite health monitoring applications


## Future Work
- Integration of time-series models (LSTM/GRU) for temporal telemetry pattern analysis
- Support for multi-satellite monitoring and fleet management
- Automatic alert threshold calibration based on historical data
- Integration with real telemetry streams from satellite ground stations
- Enhanced anomaly detection using unsupervised learning techniques
- Mobile application for remote monitoring capabilities


## Project Structure
```
satellite-telemetry-health-prediction/
│
├── data/
│   └── telemetry_data.csv              # Simulated satellite telemetry dataset
│
├── notebooks/
│   └── satellite_telemetry_model.ipynb # Main ML pipeline and model training
│
├── app/
│   └── gradio_dashboard.py             # Interactive dashboard application
│
├── requirements.txt                     # Python dependencies
└── README.md                            # Project documentation
```


## Getting Started

### Prerequisites
```bash
Python 3.7+
pip package manager
```

### Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/satellite-telemetry-health-prediction.git
cd satellite-telemetry-health-prediction
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Run the Jupyter notebook to train models:
```bash
jupyter notebook notebooks/satellite_telemetry_model.ipynb
```

4. Launch the dashboard:
```bash
python app/gradio_dashboard.py
```


## Usage Example
Once the dashboard is running, input telemetry parameters such as:
- Communication signal strength
- Power system voltage
- Thermal sensor readings
- System load metrics

The system will instantly provide:
- **Alert Probability**: Likelihood of anomaly occurrence
- **Health Score**: Overall satellite health rating (0-100)
- **Status Category**: NORMAL, WARNING, or CRITICAL


## Contributing
Contributions are welcome! Please feel free to submit a Pull Request or open an Issue for any improvements or bug fixes.


## Acknowledgments
- Inspired by ISRO Master Control Facility (MCF) operations
- Built for educational and research purposes in satellite telemetry analysis
- Thanks to the open-source community for the amazing tools and libraries


## Contact
For questions or collaboration opportunities, please reach out via [GitHub Issues](https://github.com/rajatDpatil/satellite-telemetry-health-prediction/issues).


** If you find this project useful, please consider giving it a star!**
