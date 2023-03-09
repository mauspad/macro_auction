% Script: RQ_bidding_run_analyses.m
% Created by Emily Perszyk on 12/16/22
% Goal: To compile the macro data
% Inputs: data output from "RQ_bidding_compile_data.m" script
% Be sure to update the locations of the files you are bringing in if needed (see comments that read "UPDATE PATH")

%% Set-up

clear all

% Bring in the data 
% UNCOMMENT DATA TYPE you want to load (option #1 or #2)

% Option #1:
load /Users/eep29/Desktop/Xue_macro/1_Compile_data/RQ_bid_data_dec21_2022.mat % should include both data and av_data tables

% Option #2: 
% data = readtable('/Users/eep29/Desktop/Xue_macro/1_Compile_data/RQ_bid_data_dec21_2022.csv');
% av_data = readtable('/Users/eep29/Desktop/Xue_macro/1_Compile_data/Average_RQ_bid_data_dec21_2022.csv');

%% Data exclusions for bidding too many zeros

% Exclude subjects who bid an average of zero for 20+ foods 
data(data.NumZeroBids>=20,:)=[];
av_data(av_data.NumZeroBids>=20,:)=[];

% Exclude subjects with RQ<0.70
data(data.RQ<0.7,:)=[];
av_data(av_data.RQ<0.7,:)=[];

%% Test for RQ x nutrient interaction on bid amount (Categorical predictors for fat/carb content)

% --- Test FAT content --- % 
data.FatCat(data.Fat>=median(data.Fat),:)='1'; % high fat
data.FatCat(data.Fat<median(data.Fat),:)='0'; % low fat
data.FatCat = nominal(data.FatCat);
lme1 = fitlme(data,'Bid~RQ*FatCat+BMI+Sex+Age+(1|Subject)');
lme1_anova = anova(lme1); % RQ x FatCat interaction: p = 0.0015

% Test in individuals with low RQ
data_low_RQ = data(data.RQ<=median(data.RQ),:);
lme1 = fitlme(data_low_RQ,'Bid~FatCat+BMI+Sex+Age+(1|Subject)');
lme1_anova = anova(lme1); % FatCat: p = 0.0146

% Test in individuals with high RQ
data_high_RQ = data(data.RQ>median(data.RQ),:);
lme1 = fitlme(data_high_RQ,'Bid~FatCat+BMI+Sex+Age+(1|Subject)');
lme1_anova = anova(lme1); % FatCat: p = 0.0014

% --- Test CARB content --- % 
data.CarbCat(data.Carb>=median(data.Carb),:)='1'; % high carb
data.CarbCat(data.Carb<median(data.Carb),:)='0'; % low carb
data.CarbCat = nominal(data.CarbCat);
lme1 = fitlme(data,'Bid~RQ*CarbCat+BMI+Sex+Age+(1|Subject)');
lme1_anova = anova(lme1); % RQ x CarbCat interaction: p = 0.0019

% Test in individuals with low RQ
data_low_RQ = data(data.RQ<=median(data.RQ),:);
lme1 = fitlme(data_low_RQ,'Bid~CarbCat+BMI+Sex+Age+(1|Subject)');
lme1_anova = anova(lme1); % CarbCat: p = 0.0153

% Test in individuals with high RQ
data_high_RQ = data(data.RQ>median(data.RQ),:);
lme1 = fitlme(data_high_RQ,'Bid~CarbCat+BMI+Sex+Age+(1|Subject)');
lme1_anova = anova(lme1); % CarbCat: p = 0.0008

%% Create some averages based on low/high RQ for plots

av_data_low_RQ_foods = table;
av_data_low_RQ_foods.FoodIndex=[0:35]';
av_data_high_RQ_foods = table;
av_data_high_RQ_foods.FoodIndex=[0:35]';

for item = 0:35
    av_data_low_RQ_foods.Bid(av_data_low_RQ_foods.FoodIndex==item,:) = mean(data_low_RQ.Bid(data_low_RQ.FoodIndex==item,:),'omitnan');
    av_data_low_RQ_foods.Fat(av_data_low_RQ_foods.FoodIndex==item,:) = mean(data_low_RQ.Fat(data_low_RQ.FoodIndex==item,:),'omitnan');
    av_data_low_RQ_foods.Carb(av_data_low_RQ_foods.FoodIndex==item,:) = mean(data_low_RQ.Carb(data_low_RQ.FoodIndex==item,:),'omitnan');
    av_data_high_RQ_foods.Bid(av_data_high_RQ_foods.FoodIndex==item,:) = mean(data_high_RQ.Bid(data_high_RQ.FoodIndex==item,:),'omitnan');
    av_data_high_RQ_foods.Fat(av_data_high_RQ_foods.FoodIndex==item,:) = mean(data_high_RQ.Fat(data_high_RQ.FoodIndex==item,:),'omitnan');
    av_data_high_RQ_foods.Carb(av_data_high_RQ_foods.FoodIndex==item,:) = mean(data_high_RQ.Carb(data_high_RQ.FoodIndex==item,:),'omitnan');
end 

%% Test for RQ x nutrient interaction on bid amount (Continuous predictors for fat/carb content)

% --- Test FAT content --- % 
lme1 = fitlme(data,'Bid~RQ*Fat+BMI+Sex+Age+(1|Subject)');
lme1_anova = anova(lme1); % RQ x Fat interaction: p = 0.0033

% Test in individuals with low RQ
data_low_RQ = data(data.RQ<=median(data.RQ),:);
lme1 = fitlme(data_low_RQ,'Bid~Fat+BMI+Sex+Age+(1|Subject)');
lme1_anova = anova(lme1); % Fat: ns

% Test in individuals with high RQ
data_high_RQ = data(data.RQ>median(data.RQ),:);
lme1 = fitlme(data_high_RQ,'Bid~Fat+BMI+Sex+Age+(1|Subject)');
lme1_anova = anova(lme1); % Fat: p < 0.0001

% --- Test CARB content --- % 
lme1 = fitlme(data,'Bid~RQ*Carb+BMI+Sex+Age+(1|Subject)');
lme1_anova = anova(lme1); % RQ x CarbCat interaction: p = 0.0023

% Test in individuals with low RQ
data_low_RQ = data(data.RQ<=median(data.RQ),:);
lme1 = fitlme(data_low_RQ,'Bid~Carb+BMI+Sex+Age+(1|Subject)');
lme1_anova = anova(lme1); % Carb: ns

% Test in individuals with high RQ
data_high_RQ = data(data.RQ>median(data.RQ),:);
lme1 = fitlme(data_high_RQ,'Bid~Carb+BMI+Sex+Age+(1|Subject)');
lme1_anova = anova(lme1); % Carb: p = 0.0001
