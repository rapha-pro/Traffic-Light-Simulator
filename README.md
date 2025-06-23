# 🚦 Traffic Light Prediction System

> **Predicting traffic light states and timing to optimize vehicle routing and fuel efficiency**

A machine learning system that helps vehicles adjust speed to "catch green lights" - reducing fuel consumption, emissions, and travel time. Built using real German highway driving data and designed for integration with autonomous driving systems.

<!-- ## 🎯 Business Impact

**Target Applications:**
- Navigation apps (Google Maps, Waze)
- Tesla Full Self-Driving (FSD)
- Ford BlueCruise
- Mercedes Drive Pilot
- Fleet management systems

**Value Proposition:**
- **10-15% fuel savings** through speed optimization
- **20% reduction** in stop-and-go traffic
- **Improved driver experience** with smoother journeys
- **Environmental impact** through reduced emissions

## 🛠️ Technical Approach

### Data Foundation
- **Real-world data**: HighD German highway dataset (25Hz vehicle trajectories)
- **Smart placement**: Traffic lights positioned using actual deceleration patterns
- **Realistic simulation**: German traffic light timing standards

### Machine Learning Pipeline
- **Multi-output prediction**: Simultaneous light color + timing prediction
- **Feature engineering**: Distance, approach time, traffic density, weather
- **Model ensemble**: Random Forest + XGBoost + LSTM for robustness
- **Real-time inference**: <100ms prediction latency

### Key Innovations
1. **Deceleration-based placement** - Traffic lights where drivers naturally slow down
2. **Multi-modal features** - Vehicle dynamics + infrastructure + environmental data
3. **Business-focused metrics** - Fuel savings and time efficiency quantification
4. **Automotive-ready** - Designed for V2X communication integration -->

<!-- ## 📊 Results Summary

| Metric | Target | Achieved |
|--------|--------|----------|
| Classification Accuracy | >85% | 87.3% |
| Timing Prediction (MAE) | <5 seconds | 3.2 seconds |
| Fuel Savings | >10% | 12.4% |
| Time Savings | >15% | 18.7% |
| Inference Speed | <100ms | 67ms | -->

## 🗂️ Project Structure

```
traffic_light_predictor/
├── 📄 README.md                     # Project overview (you are here)
├── 📊 data/
│   ├── raw/highd/                   # Original HighD dataset
│   ├── processed/                   # Cleaned and engineered data
│   └── results/                     # Model outputs and metrics
├── 📓 notebooks/                    # Analysis and development
│   ├── README.md                    # Notebook documentation
│   ├── 01_eda_basic.ipynb           # Data exploration
│   ├── 02_traffic_light_placement.ipynb
│   ├── 03_simulation_data_generation.ipynb
│   ├── 04_feature_engineering.ipynb
│   ├── 05_model_training.ipynb
│   └── 06_model_evaluation.ipynb
├── 🐍 src/                          # Production code
│   ├── data_processing/             # Data pipeline modules
│   ├── models/                      # ML model implementations
│   └── visualization/               # Plotting and dashboard utils
├── 🚀 streamlit_app/                # Interactive demo
│   └── app.py                       # Traffic light prediction dashboard
├── 🧪 tests/                        # Unit tests
├── 📋 requirements.txt              # Python dependencies
└── 🚫 .gitignore                    # Git ignore rules
```

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- 8GB RAM minimum :)
- HighD dataset (download from [official source](https://www.highd-dataset.com/))

### Installation
```bash
git clone https://github.com/rapha-pro/Traffic-Light-Simulator.git
cd traffic_light_predictor

# Install dependencies with pipenv
pipenv install

# Activate virtual environment
pipenv shell

# Download and extract HighD data to data/raw/highd/
```

### Run Analysis
```bash
# Start Jupyter
jupyter notebook

# Follow notebooks in order:
# 1. notebooks/01_eda_basic.ipynb
# 2. notebooks/02_traffic_light_placement.ipynb
# 3. ... (see notebooks/README.md for full sequence)
```

### Interactive Demo
```bash
streamlit run streamlit_app/app.py
```

<!-- ## 📈 Model Performance

### Classification Results (Next Light Color)
- **Overall Accuracy**: 87.3%
- **Precision**: Red: 0.89, Yellow: 0.82, Green: 0.91
- **Recall**: Red: 0.91, Yellow: 0.79, Green: 0.89

### Regression Results (Time to Change)
- **Mean Absolute Error**: 3.2 seconds
- **R² Score**: 0.84
- **95% Predictions within**: ±7 seconds

### Business Impact
- **Fuel Efficiency**: 12.4% improvement vs baseline
- **Travel Time**: 18.7% reduction in delays
- **Success Rate**: 94% of recommendations lead to green lights

## 🛣️ Use Cases

### 1. Autonomous Vehicles
```python
# Integration example
prediction = model.predict({
    'distance_to_light': 150,  # meters
    'current_speed': 60,       # km/h
    'traffic_density': 0.7     # ratio
})
# Output: {'next_state': 'green', 'time_to_change': 8.3}
```

### 2. Navigation Apps
- Route optimization considering traffic light timing
- Speed recommendations for fuel efficiency
- Real-time traffic flow optimization

### 3. Fleet Management
- Delivery route optimization
- Driver coaching for eco-driving
- Predictive maintenance based on driving patterns

## 🔬 Technical Deep Dive

### Data Pipeline
1. **Raw Data**: HighD highway trajectories (25Hz, 50+ vehicles)
2. **Feature Engineering**: 47 features including vehicle dynamics, spatial relationships
3. **Target Creation**: Light states + timing from realistic simulation
4. **Model Training**: Ensemble approach with cross-validation

### Key Features
- `distance_to_light`: Spatial relationship to intersection
- `approach_time`: Time to reach light at current speed
- `traffic_density`: Surrounding vehicle count
- `historical_timing`: Past light cycle patterns
- `weather_conditions`: Environmental factors

### Model Architecture
- **Base Models**: Random Forest, XGBoost, Support Vector Regression
- **Ensemble**: Weighted voting based on validation performance
- **Time Series**: LSTM for temporal pattern recognition
- **Deployment**: ONNX format for cross-platform inference

## 📊 Data Sources

- **Primary**: HighD Dataset (German highway driving data)
- **Supplementary**: Traffic light timing standards (German regulations)
- **Validation**: Real-world intersection data (open city datasets) -->

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

### License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

## Acknowledgments

- **HighD Dataset**: Institute for Automotive Engineering (ika), RWTH Aachen University
- **Inspiration**: Real-world need for fuel-efficient autonomous driving
- **Target**: Contributing to sustainable transportation technology


<!-- **⭐ If this project helped you, please consider giving it a star!** -->
