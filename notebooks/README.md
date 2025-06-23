# 📓 Analysis Notebooks

> **Step-by-step data science workflow from raw data to production models**

This directory contains the complete analytical journey for the Traffic Light Prediction System. Each notebook builds upon the previous, creating a reproducible ML pipeline.

## 🎯 Workflow Overview

```mermaid
graph LR
    A[HighD Data] --> B[01_EDA]
    B --> C[02_Placement]
    C --> D[03_Simulation]
    D --> E[04_Features]
    E --> F[05_Training]
    F --> G[06_Evaluation]
    G --> H[Production Model]
```

## 📚 Notebook Sequence

### 📊 01_eda_basic.ipynb
**Exploratory Data Analysis**

**Purpose**: Understand HighD dataset structure and validate suitability for traffic simulation

**Key Outputs**:
- Data quality assessment
- Speed and behavior patterns
- Highway characteristics
- Simulation design parameters

**Runtime**: ~15 minutes | **Data In**: Raw HighD files | **Data Out**: `highd_cleaned.csv`

---

### 🚦 02_traffic_light_placement.ipynb  
**Traffic Light Placement Strategy**

**Purpose**: Identify optimal intersection locations using real deceleration patterns

**Methodology**:
- Calculate vehicle deceleration events
- Spatial clustering analysis
- Traffic engineering validation

**Runtime**: ~20 minutes | **Data In**: `highd_cleaned.csv` | **Data Out**: `traffic_light_locations.csv`

---

<!-- ### 🎯 03_simulation_data_generation.ipynb
**Traffic Light Timing Simulation**

**Purpose**: Generate realistic traffic light cycles and merge with vehicle trajectories

**Features**:
- German traffic light standards
- Time-of-day variations
- Weather impact modeling

**Runtime**: ~25 minutes | **Data In**: Vehicle + location data | **Data Out**: `simulated_light_cycles.csv`

---

### ⚙️ 04_feature_engineering.ipynb
**ML Feature Creation**

**Purpose**: Transform raw data into ML-ready features with proper train/test splits

**Created Features**:
- Spatial: `distance_to_light`, `lane_position`
- Temporal: `approach_time`, `time_to_change`
- Behavioral: `traffic_density`, `speed_consistency`

**Runtime**: ~30 minutes | **Data In**: Simulated data | **Data Out**: `training_features.csv`

---

### 🤖 05_model_training.ipynb
**Machine Learning Model Development**

**Purpose**: Train and optimize models for traffic light state and timing prediction

**Models Tested**:
- Random Forest (baseline)
- XGBoost (performance)
- LSTM (time-series)
- Ensemble (production)

**Runtime**: ~45 minutes | **Data In**: Feature data | **Data Out**: Trained models

---

### 📈 06_model_evaluation.ipynb
**Model Validation & Business Impact**

**Purpose**: Comprehensive testing and business value quantification

**Evaluation Areas**:
- Technical metrics (accuracy, MAE, F1)
- Business impact (fuel savings, time efficiency)
- Robustness testing (edge cases, cross-validation)

**Runtime**: ~20 minutes | **Data In**: Models + test data | **Data Out**: Performance reports -->

## 🛠️ Usage Instructions

### Prerequisites
```bash
# Ensure you're in the project root
cd traffic_light_predictor

# Activate virtual environment
pipenv shell

# Download and extract HighD data to data/raw/highd/
```

### Execution Order
**⚠️ Important**: Run notebooks in numerical order. Each depends on outputs from previous notebooks.

1. **Start with 01_eda_basic.ipynb** - establishes data foundation
2. **Continue sequentially** - don't skip notebooks
3. **Check outputs** - verify each notebook produces expected files
4. **Monitor runtime** - longer notebooks indicate more complex processing

<!-- ### Data Dependencies
```
data/
├── raw/highd/                    ← Required: Download HighD dataset first
├── processed/                    ← Generated: Created by notebooks
│   ├── highd_cleaned.csv         ← From: 01_eda_basic.ipynb
│   ├── traffic_light_locations.csv ← From: 02_traffic_light_placement.ipynb
│   ├── simulated_light_cycles.csv ← From: 03_simulation_data_generation.ipynb
│   ├── training_features.csv     ← From: 04_feature_engineering.ipynb
│   └── trained_models/           ← From: 05_model_training.ipynb
└── results/                      ← Generated: Final outputs
```

## 🎓 Learning Objectives

### Technical Skills Demonstrated
- **Data Engineering**: Real-world data cleaning and validation
- **Feature Engineering**: Domain-specific feature creation
- **Model Selection**: Comparing multiple ML approaches
- **Evaluation**: Technical and business metrics
- **Documentation**: Professional project organization

### Domain Knowledge Applied
- **Traffic Engineering**: Understanding traffic light timing standards
- **Automotive Systems**: Vehicle dynamics and driver behavior
- **Optimization**: Fuel efficiency and route planning
- **Simulation**: Realistic traffic scenario generation

## 🚨 Troubleshooting

### Common Issues

**"File not found" errors**:
- Ensure you're running from `notebooks/` directory
- Check that previous notebooks completed successfully
- Verify data files exist in expected locations

**Memory issues**:
- Close other applications
- Restart Jupyter kernel between notebooks
- Consider using data sampling for initial development

**Long runtime**:
- Some notebooks are computationally intensive
- Consider reducing data size for testing
- Use progress bars to monitor completion

### Getting Help
1. **Review data outputs** - ensure previous steps completed correctly
2. **Validate environment** - confirm all packages installed correctly

## 📊 Expected Results

### Data Volumes
- **Raw data**: ~500MB HighD files
- **Processed data**: ~200MB cleaned datasets
- **Model files**: ~50MB trained models
- **Total storage**: ~1GB project size -->

<!-- ### Performance Benchmarks
- **01_EDA**: Basic stats, 4-5 visualizations
- **02_Placement**: 8-12 traffic light locations identified
- **03_Simulation**: 50K+ simulated light state records
- **04_Features**: 47 engineered features, 80/20 train/test split
- **05_Training**: 85%+ accuracy models
- **06_Evaluation**: Comprehensive performance report -->

### Best Practices
- **Save frequently** - notebooks can be fragile
- **Clear outputs** before committing to Git
- **Add markdown** explanations for complex code
- **Use meaningful variable names**
