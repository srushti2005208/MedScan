#!/usr/bin/env python
"""Test script to verify patient name and diagnosis extraction"""

import sys
import os

# Add backend directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

# Test the extraction functions
from analyzer_IMPROVED import MedicalReportAnalyzer

# Sample medical report text
sample_report = """
MEDICAL LABORATORY REPORT
Patient Name: John Smith
Age: 45
Gender: Male
Date: 2024-02-26

CLINICAL DIAGNOSIS
- Type 2 Diabetes Mellitus
- Hypertension
- Hyperlipidemia

BLOOD TEST RESULTS
Hemoglobin: 13.5 g/dL (Normal)
Blood Glucose: 180 mg/dL (High)
Total Cholesterol: 250 mg/dL (High)
Systolic Blood Pressure: 160 mmHg (High)
Diastolic Blood Pressure: 95 mmHg (High)
Heart Rate: 78 bpm (Normal)
Oxygen Saturation: 98% (Normal)

IMPRESSION
Patient shows signs of elevated blood sugar and high cholesterol, consistent with diabetes 
and metabolic syndrome. Hypertension also noted.
"""

# Test extraction
analyzer = MedicalReportAnalyzer()

# Manually test extraction methods
print("=" * 60)
print("EXTRACTION TEST RESULTS")
print("=" * 60)

# Test patient name
name = analyzer._extract_patient_name(sample_report)
print(f"✓ Patient Name: {name}")

# Test patient age
age = analyzer._extract_patient_age(sample_report)
print(f"✓ Patient Age: {age}")

# Test patient gender
gender = analyzer._extract_patient_gender(sample_report)
print(f"✓ Patient Gender: {gender}")

# Test diagnoses
analyzer.extracted_text = sample_report.lower()
diagnoses = analyzer._extract_diagnoses(sample_report)
print(f"✓ Diagnoses Found: {len(diagnoses)}")
for d in diagnoses:
    print(f"  - {d}")

# Test vitals extraction
vitals = analyzer._extract_vitals(sample_report)
print(f"\n✓ Vitals Found: {len(vitals)}")
for v in vitals[:8]:
    print(f"  - {v['parameter']}: {v['value']} {v['unit']} ({v['status']})")

print("\n" + "=" * 60)
print("EXTRACTION TEST COMPLETED SUCCESSFULLY!")
print("=" * 60)
