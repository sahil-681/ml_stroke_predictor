Data1: Treatments done on dataset 5k_stroke-data.csv

1-'Other' value removed from 'gender' since only 1 entry
2-Label encoding done of categorical variables
	-gender: 1=male, 0=female
	-ever_married: 1=yes,0=no
	-work_type: 0=Govt_job,1=Never_worked,2=Private,3=Self-employed,4=children
	-Residence_type: 0=rural,1=urban
	-smoking_status: 0=unknown,1=formerly smoked,2=never smoked,3=smokes
3-Handling missing values
	-Imputing 201 missing values of BMI with median
4-Oversampling of stroke positive entries
	-Stroke=1 oversampled using SMOTE and concatenated with the original database
5-File saved as Data1.csv

--x--x--x--x--x--x--

Data2: Treatments done on dataset 5k_stroke-data.csv

1-'Other' value removed from 'gender' since only 1 entry
2-Label encoding done of categorical variables
	-gender: 1=male, 0=female
	-ever_married: 1=yes,0=no
	-work_type: 0=Govt_job,1=Never_worked,2=Private,3=Self-employed,4=children
	-Residence_type: 0=rural,1=urban
	-smoking_status: 0=unknown,1=formerly smoked,2=never smoked,3=smokes
3-Handling missing values
	-Imputing 201 missing values of BMI with mean
4-Oversampling of stroke positive entries
	-Stroke=1 oversampled using SMOTE and concatenated with the original database
5-File saved as Data1_treated.csv

--x--x--x--x--x--x--

Data3: Treatments done on dataset 5k_stroke-data.csv

1-'Other' value removed from 'gender' since only 1 entry
2-Label encoding done of categorical variables
	-gender: 1=male, 0=female
	-ever_married: 1=yes,0=no
	-work_type: 0=Govt_job,1=Never_worked,2=Private,3=Self-employed,4=children
	-Residence_type: 0=rural,1=urban
	-smoking_status: 0=unknown,1=formerly smoked,2=never smoked,3=smokes
3-Handling missing values
	-Imputing 201 missing values of BMI with mode
4-Oversampling of stroke positive entries
	-Stroke=1 oversampled using SMOTE and concatenated with the original database
5-File saved as Data3_treated.csv

--x--x--x--x--x--x--

Data3-0: Treatments done on dataset 5k_stroke-data.csv

1-'Other' value removed from 'gender' since only 1 entry
2-Label encoding done of categorical variables
	-gender: 1=male, 0=female
	-ever_married: 1=yes,0=no
	-work_type: 0=Govt_job,1=Never_worked,2=Private,3=Self-employed,4=children
	-Residence_type: 0=rural,1=urban
	-smoking_status: 0=unknown,1=formerly smoked,2=never smoked,3=smokes
3-Handling missing values
	-Imputing 201 missing values of BMI with mode
4-Removed columns 'id'
5-Oversampling of stroke positive entries
	-Stroke=1 oversampled using SMOTE and concatenated with the original database
6-File saved as Data3-0_treated.csv

--x--x--x--x--x--x--

Data3-1: Treatments done on dataset 5k_stroke-data.csv

1-'Other' value removed from 'gender' since only 1 entry
2-Label encoding done of categorical variables
	-gender: 1=male, 0=female
	-ever_married: 1=yes,0=no
	-work_type: 0=Govt_job,1=Never_worked,2=Private,3=Self-employed,4=children
	-Residence_type: 0=rural,1=urban
	-smoking_status: 0=unknown,1=formerly smoked,2=never smoked,3=smokes
3-Handling missing values
	-Imputing 201 missing values of BMI with mode
4-Removed columns 'id' 
5-Dropped outliers in 'age','avg_glucose_level','bmi'
6-Oversampling of stroke positive entries
	-Stroke=1 oversampled using SMOTE and concatenated with the original database
7-File saved as Data3-1_treated.csv

--x--x--x--x--x--x--

Data 3-2:Treatments done on dataset 5k_stroke-data.csv

1-'Other' value removed from 'gender' since only 1 entry
2-Label encoding done of categorical variables
	-gender: 1=male, 0=female
	-ever_married: 1=yes,0=no
	-work_type: 0=Govt_job,1=Never_worked,2=Private,3=Self-employed,4=children
	-Residence_type: 0=rural,1=urban
	-smoking_status: 0=unknown,1=formerly smoked,2=never smoked,3=smokes
3-Handling missing values
	-Imputing 201 missing values of BMI with mode
4-Removed columns 'id'
5-Treated outliers in 'age','avg_glucose_level','bmi' by replacement with mode
6-Oversampling of stroke positive entries
	-Stroke=1 oversampled using SMOTE and concatenated with the original database
7-File saved as Data3-2_treated.csv

--x--x--x--x--x--x--

Data3-3: Treatments done on dataset 5k_stroke-data.csv

1-'Other' value removed from 'gender' since only 1 entry
2-Label encoding done of categorical variables
	-gender: 1=male, 0=female
	-ever_married: 1=yes,0=no
	-work_type: 0=Govt_job,1=Never_worked,2=Private,3=Self-employed,4=children
	-Residence_type: 0=rural,1=urban
	-smoking_status: 0=unknown,1=formerly smoked,2=never smoked,3=smokes
3-Handling missing values
	-Imputing 201 missing values of BMI with mode
4-Removed columns 'id' and 'Residence_type'
5-Treated outliers in 'age','avg_glucose_level','bmi' by replacement with mode
6-Oversampling of stroke positive entries
	-Stroke=1 oversampled using SMOTE and concatenated with the original database
7-File saved as Data3-3_treated.csv

--x--x--x--x--x--x--

Data3-3_treated.csv was finally used to train a Machine Learning Classification Model, which has been used to build the web application: https://bit.ly/ml-stroke-predictor-sahil
