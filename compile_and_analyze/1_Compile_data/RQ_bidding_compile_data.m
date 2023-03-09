% Script: RQ_bidding_compile_data.m
% Created by Emily Perszyk on 12/16/22
% Goal: To compile the data for testing RQ vs bidding (and accounting for other variables)
% Inputs: auction task bids for 2 runs, food ratings, estimated price csv files
% Outputs: data (individual ratings per person and food) and av_data (averages per macro category per person)
% Be sure to update the locations of the files you are bringing in if needed (see comments that read "UPDATE PATH")
% Be sure to update any subjects with missing data (see comments that read "UPDATE MISSING SUBJECTS")
% Be sure to update how you would like the data to be saved (see comment that reads "UNCOMMENT TO SAVE DATA")
   
%% Bring in the auction run 1 data

clear all;

% Point to where the .csv files are located
files = dir('/Users/eep29/Desktop/Xue_macro/1_Compile_data/Auction/*.csv'); % UPDATE PATH
files(2:2:end,:) = []; % since all the data is in one big folder, this will keep only the first file for each person (aka run 1); below we will keep only run 2
auction1 = table; % table to store the auction run 1 data
num=length(files);

%Row numbers
row2=0;
row1=1;
for i = 1:num % loop through all of the files in the designated folder

    tmp_subdata = readtable(fullfile(files(i).folder, files(i).name)); % temporarily store each subject's data
    tmp_subdata(isnan(tmp_subdata.bid_items_thisTrialN),:)=[]; % remove any rows that aren't real trials
    row2=row2+height(tmp_subdata); % read through all 36 trials per subject
    auction1.Subject(row1:row2,1) = tmp_subdata.participant;
    auction1.ImageFile(row1:row2,1)=tmp_subdata.image_file;
    auction1.FoodType(row1:row2,1)=tmp_subdata.foodtype;
    auction1.Bid1(row1:row2,1)=tmp_subdata.Bid;
    auction1.BidRT1(row1:row2,1)=tmp_subdata.Bid_RT; % reaction time in seconds
    row1=row1++height(tmp_subdata);

    %Create a table with all subject IDs
    tmp_sub=files(i).name;
    subjects(i,1)= str2num(tmp_sub(1,1:4));
    clear tmp_subdata

end

%% Bring in the auction run 2 data

% Point to where the .csv files are located
files = dir('/Users/eep29/Desktop/Xue_macro/1_Compile_data/Auction/*.csv'); % UPDATE PATH
files(1:2:end,:) = []; % since all the data is in one big folder, this will keep only the first file for each person (aka run 1); below we will keep only run 2
auction2 = table; % table to store the auction run 2 data
num=length(files);

%Row numbers
row2=0;
row1=1;
for i = 1:num % loop through all of the files in the designated folder

    tmp_subdata = readtable(fullfile(files(i).folder, files(i).name)); % temporarily store each subject's data
    tmp_subdata(isnan(tmp_subdata.bid_items_thisTrialN),:)=[]; % remove any rows that aren't real trials
    row2=row2+height(tmp_subdata); % read through all 36 trials per subject
    auction2.Subject(row1:row2,1) = tmp_subdata.participant;
    auction2.ImageFile(row1:row2,1)=tmp_subdata.image_file;
    auction2.Bid2(row1:row2,1)=tmp_subdata.Bid;
    auction2.BidRT2(row1:row2,1)=tmp_subdata.Bid_RT; % reaction time in seconds
    row1=row1++height(tmp_subdata);

end

%% Match the correct food index to each food item for auction data

food_properties = readtable('Food_properties.xlsx');
data = join(auction1, auction2, 'Keys', {'Subject','ImageFile'}); % join two tables at a time
data = join(data, food_properties, 'Keys', 'ImageFile'); 

%% Bring in the food ratings

% Point to where the .csv files are located
files = dir('/Users/eep29/Desktop/Xue_macro/1_Compile_data/Food_ratings/*.csv'); % UPDATE PATH
food_rating = table; % table to store the food ratings
num=length(files);

%Row numbers
row2=0;
row1=1;
for i = 1:num % loop through all of the files in the designated folder

    tmp_subdata = readtable(fullfile(files(i).folder, files(i).name)); % temporarily store each subject's data
    tmp_subdata(isnan(tmp_subdata.food_items_thisTrialN),:)=[]; % remove any rows that aren't real trials
    row2=row2+height(tmp_subdata); % read through all 36 trials per subject
    food_rating.Subject(row1:row2,1) = tmp_subdata.participant;
    food_rating.FoodIndex(row1:row2,1)=tmp_subdata.food_items_thisIndex;
    food_rating.Like(row1:row2,1) = tmp_subdata.Like;
    food_rating.Familiar(row1:row2,1) = tmp_subdata.Familiar;
    food_rating.Filling(row1:row2,1) = tmp_subdata.Filling;
    food_rating.Frequency(row1:row2,1) = tmp_subdata.Frequency;
    food_rating.Healthy(row1:row2,1) = tmp_subdata.Healthy;
    food_rating.EstimatedCalories(row1:row2,1) = tmp_subdata.calorie;
    food_rating.EstimatedEnergyDensity(row1:row2,1) = tmp_subdata.Dense;
    row1=row1++height(tmp_subdata);

end

%% Account for subjects missing the food rating data

% n = 1 currently missing food rating data
subjects_missing_food_ratings = []; % UPDATE MISSING SUBJECTS (separate IDs with a space)

% Set-up some empty variables
missing_food_rating = table;
subject_col = [];
index_col = [];
rating_col = [];

% Create a table of empty rows for these subject IDs to later merge
for subject = subjects_missing_food_ratings
    subject_col = [subject_col; repmat(subject,36,1)]; % 36 because of the 36 food items
    index_col = [index_col; repmat(0:35,1)'];
    rating_col = [rating_col; NaN(36,1)];
end 

% Add the empty rows to the missing_food_rating_table
missing_food_rating.Subject = subject_col;
missing_food_rating.FoodIndex = index_col;
missing_food_rating.Like = rating_col;
missing_food_rating.Familiar = rating_col;
missing_food_rating.Filling = rating_col;
missing_food_rating.Frequency = rating_col;
missing_food_rating.Healthy = rating_col;
missing_food_rating.EstimatedCalories = rating_col;
missing_food_rating.EstimatedEnergyDensity = rating_col;
food_rating = [food_rating; missing_food_rating];

%% Bring in the estimated price data

% Point to where the .csv files are located
files = dir('/Users/eep29/Desktop/Xue_macro/1_Compile_data/Estimated_price/*.csv'); % UPDATE PATH
estimated_price = table; % table to store the estimated price data
num=length(files);

%Row numbers
row2=0;
row1=1;
for i = 1:num % loop through all of the files in the designated folder

    tmp_subdata = readtable(fullfile(files(i).folder, files(i).name)); % temporarily store each subject's data
    tmp_subdata(isnan(tmp_subdata.food_items_thisTrialN),:)=[]; % remove any rows that aren't real trials
    row2=row2+height(tmp_subdata); % read through all 36 trials per subject
    estimated_price.Subject(row1:row2,1) = tmp_subdata.participant;
    estimated_price.FoodIndex(row1:row2,1)=tmp_subdata.food_items_thisIndex;
    estimated_price.EstimatedPrice(row1:row2,1)=tmp_subdata.Price;
    row1=row1++height(tmp_subdata);

end

%% Account for subjects missing the estimated price data

% n = 1 currently missing estimated price data
subjects_missing_estimated_price = [2665]; % UPDATE MISSING SUBJECTS (separate IDs with a space)

% Set-up some empty variables
missing_estimated_price = table;
subject_col = [];
index_col = [];
rating_col = [];

% Create a table of empty rows for these subject IDs to later merge
for subject = subjects_missing_estimated_price
    subject_col = [subject_col; repmat(subject,36,1)]; % 36 because of the 36 food items
    index_col = [index_col; repmat(0:35,1)'];
    rating_col = [rating_col; NaN(36,1)];
end 

% Add the empty rows to the missing_food_rating_table
missing_estimated_price.Subject = subject_col;
missing_estimated_price.FoodIndex = index_col;
missing_estimated_price.EstimatedPrice = rating_col;
estimated_price = [estimated_price; missing_estimated_price];

%% Join the remaining tables together

data = join(data, food_rating, 'Keys', {'Subject','FoodIndex'}); 
data = join(data, estimated_price, 'Keys', {'Subject','FoodIndex'}); 

% Clear variables we no longer need
clearvars -except data subjects

%% Recode the ratings to make them meaningful

% Remove auction data where subjects missed bidding window (previously coded as 9999)
data.Bid1(data.Bid1==9999,:)=NaN;
data.Bid2(data.Bid2==9999,:)=NaN;
data.BidRT1(data.BidRT1==9999,:)=NaN;
data.BidRT2(data.BidRT2==9999,:)=NaN;

% Recode Bids to $0-5 (currently 0-1000), and take average across the two runs
data.Bid1 = data.Bid1./200;
data.Bid2 = data.Bid2./200;
data.Bid = mean([data.Bid1,data.Bid2], 2, 'omitnan');
data.BidRT = mean([data.BidRT1,data.BidRT2], 2, 'omitnan');

% Recode Frequency to categorical 1-5 (currently 0-1000)
data.Frequency = (data.Frequency./250)+1;
% New labels are...
% 1: <1/month
% 2: 2-3/month
% 3: 1-2/month
% 4: 3-4/week
% 5: 5+/week

% Recode EstimatedCalories to 0-240 (currently 0-1000)
data.EstimatedCalories = (data.EstimatedCalories./1000)*240;

% Recode EstimatedPrice to $0-5 (currently 0-1000)
data.EstimatedPrice = data.EstimatedPrice./200;

% All other ratings are still 0-1000 (Familiar, Filling, Healthy, EstimatedEnergyDensity)
% Aside from Like which uses LHS values from -100 to +100

%% Determine the number of times each subject bid an average of zero on a food item

% Count the number of times each person bid an average of zero
for subject = subjects'
    data.NumZeroBids(data.Subject==subject,:) = repmat(sum(data.Bid==0 & data.Subject==subject),36,1);    
end

% Emily's rule of thumb was to remove subjects that bid an average of zero on 20+  items
% Not going to remove any of these people for now, but keep it in mind

%% Add a macro group categorical variable

data.FoodType=string(data.FoodType);
data.MacroGroup(data.FoodType=='fat',:) = 1;
data.MacroGroup(data.FoodType=='combo',:) = 2;
data.MacroGroup = nominal(data.MacroGroup);
% New categorical labels are...
% 0: carb
% 1: fat
% 2: combo

%% Create table with means for each subject

% Calculate averages by macro group and subject and store in separate tables
av_data = table;
av_data.Subject=subjects;

for subject = subjects'
    % Bid
    av_data.AvBid(av_data.Subject==subject,:)=mean(data.Bid(data.Subject==subject,:),'omitnan');
    av_data.AvFatBid(av_data.Subject==subject,:)=mean(data.Bid(data.Subject==subject & data.MacroGroup=='0',:),'omitnan');
    av_data.AvCarbBid(av_data.Subject==subject,:)=mean(data.Bid(data.Subject==subject & data.MacroGroup=='1',:),'omitnan');
    av_data.AvComboBid(av_data.Subject==subject,:)=mean(data.Bid(data.Subject==subject & data.MacroGroup=='2',:),'omitnan');
    % BidRT
    av_data.AvBidRT(av_data.Subject==subject,:)=mean(data.BidRT(data.Subject==subject,:),'omitnan');
    av_data.AvFatBidRT(av_data.Subject==subject,:)=mean(data.BidRT(data.Subject==subject & data.MacroGroup=='0',:),'omitnan');
    av_data.AvCarbBidRT(av_data.Subject==subject,:)=mean(data.BidRT(data.Subject==subject & data.MacroGroup=='1',:),'omitnan');
    av_data.AvComboBidRT(av_data.Subject==subject,:)=mean(data.BidRT(data.Subject==subject & data.MacroGroup=='2',:),'omitnan');
    % Like
    av_data.AvLike(av_data.Subject==subject,:)=mean(data.Like(data.Subject==subject,:),'omitnan');
    av_data.AvFatLike(av_data.Subject==subject,:)=mean(data.Like(data.Subject==subject & data.MacroGroup=='0',:),'omitnan');
    av_data.AvCarbLike(av_data.Subject==subject,:)=mean(data.Like(data.Subject==subject & data.MacroGroup=='1',:),'omitnan');
    av_data.AvComboLike(av_data.Subject==subject,:)=mean(data.Like(data.Subject==subject & data.MacroGroup=='2',:),'omitnan');
    % Familiar
    av_data.AvFamiliar(av_data.Subject==subject,:)=mean(data.Familiar(data.Subject==subject,:),'omitnan');
    av_data.AvFatFamiliar(av_data.Subject==subject,:)=mean(data.Familiar(data.Subject==subject & data.MacroGroup=='0',:),'omitnan');
    av_data.AvCarbFamiliar(av_data.Subject==subject,:)=mean(data.Familiar(data.Subject==subject & data.MacroGroup=='1',:),'omitnan');
    av_data.AvComboFamiliar(av_data.Subject==subject,:)=mean(data.Familiar(data.Subject==subject & data.MacroGroup=='2',:),'omitnan');
    % Filling
    av_data.AvFilling(av_data.Subject==subject,:)=mean(data.Filling(data.Subject==subject,:),'omitnan');
    av_data.AvFatFilling(av_data.Subject==subject,:)=mean(data.Filling(data.Subject==subject & data.MacroGroup=='0',:),'omitnan');
    av_data.AvCarbFilling(av_data.Subject==subject,:)=mean(data.Filling(data.Subject==subject & data.MacroGroup=='1',:),'omitnan');
    av_data.AvComboFilling(av_data.Subject==subject,:)=mean(data.Filling(data.Subject==subject & data.MacroGroup=='2',:),'omitnan');
    % Frequency
    av_data.AvFrequency(av_data.Subject==subject,:)=mean(data.Frequency(data.Subject==subject,:),'omitnan');
    av_data.AvFatFrequency(av_data.Subject==subject,:)=mean(data.Frequency(data.Subject==subject & data.MacroGroup=='0',:),'omitnan');
    av_data.AvCarbFrequency(av_data.Subject==subject,:)=mean(data.Frequency(data.Subject==subject & data.MacroGroup=='1',:),'omitnan');
    av_data.AvComboFrequency(av_data.Subject==subject,:)=mean(data.Frequency(data.Subject==subject & data.MacroGroup=='2',:),'omitnan');
    % Healthy
    av_data.AvHealthy(av_data.Subject==subject,:)=mean(data.Healthy(data.Subject==subject,:),'omitnan');
    av_data.AvFatHealthy(av_data.Subject==subject,:)=mean(data.Healthy(data.Subject==subject & data.MacroGroup=='0',:),'omitnan');
    av_data.AvCarbHealthy(av_data.Subject==subject,:)=mean(data.Healthy(data.Subject==subject & data.MacroGroup=='1',:),'omitnan');
    av_data.AvComboHealthy(av_data.Subject==subject,:)=mean(data.Healthy(data.Subject==subject & data.MacroGroup=='2',:),'omitnan');    
    % EstimatedCalories
    av_data.AvEstimatedCalories(av_data.Subject==subject,:)=mean(data.EstimatedCalories(data.Subject==subject,:),'omitnan');
    av_data.AvFatEstimatedCalories(av_data.Subject==subject,:)=mean(data.EstimatedCalories(data.Subject==subject & data.MacroGroup=='0',:),'omitnan');
    av_data.AvCarbEstimatedCalories(av_data.Subject==subject,:)=mean(data.EstimatedCalories(data.Subject==subject & data.MacroGroup=='1',:),'omitnan');
    av_data.AvComboEstimatedCalories(av_data.Subject==subject,:)=mean(data.EstimatedCalories(data.Subject==subject & data.MacroGroup=='2',:),'omitnan');    
    % EstimatedEnergyDensity
    av_data.AvEstimatedEnergyDensity(av_data.Subject==subject,:)=mean(data.EstimatedEnergyDensity(data.Subject==subject,:),'omitnan');
    av_data.AvFatEstimatedEnergyDensity(av_data.Subject==subject,:)=mean(data.EstimatedEnergyDensity(data.Subject==subject & data.MacroGroup=='0',:),'omitnan');
    av_data.AvCarbEstimatedEnergyDensity(av_data.Subject==subject,:)=mean(data.EstimatedEnergyDensity(data.Subject==subject & data.MacroGroup=='1',:),'omitnan');
    av_data.AvComboEstimatedEnergyDensity(av_data.Subject==subject,:)=mean(data.EstimatedEnergyDensity(data.Subject==subject & data.MacroGroup=='2',:),'omitnan');    
    % EstimatedPrice
    av_data.AvEstimatedPrice(av_data.Subject==subject,:)=mean(data.EstimatedPrice(data.Subject==subject,:),'omitnan');
    av_data.AvFatEstimatedPrice(av_data.Subject==subject,:)=mean(data.EstimatedPrice(data.Subject==subject & data.MacroGroup=='0',:),'omitnan');
    av_data.AvCarbEstimatedPrice(av_data.Subject==subject,:)=mean(data.EstimatedPrice(data.Subject==subject & data.MacroGroup=='1',:),'omitnan');
    av_data.AvComboEstimatedPrice(av_data.Subject==subject,:)=mean(data.EstimatedPrice(data.Subject==subject & data.MacroGroup=='2',:),'omitnan');
    % NumZeroBids
    av_data.NumZeroBids(av_data.Subject==subject,:)=mean(data.NumZeroBids(data.Subject==subject,:),'omitnan');
end

%% Bring in the subject vars data (e.g., BMI, sex, age, etc.)

vars = readtable('RQ_bid_subject_vars.xlsx');

% Join the tables
data = join(data, vars, 'Keys', 'Subject'); % join two tables at a time
av_data = join(av_data, vars, 'Keys', 'Subject');

%% Write outputs to excel files (comment out if looping into another matlab script)

clearvars -except data av_data

% UNCOMMENT TO SAVE DATA
% Remove the % symbol from any of the below (and rename file) to save the data as a .csv file or a .mat file

% save RQ_bid_data_dec21_2022.mat
% writetable(data,'RQ_bid_data_dec21_2022.csv');
% writetable(av_data,'Average_RQ_bid_data_dec21_2022.csv');
