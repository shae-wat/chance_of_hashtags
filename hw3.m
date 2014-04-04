%hw3

load hw3_netflix.mat

%=======Assignment parameters=======
u = 1978; %number users
m=4635; %number movies
k = 10; %number genres
iterations = 30;
lambda = 0.5; %****
I = eye(k,k); %****

%=======Learn M and U given R=======

U = randn(u,k);
M = randn(k,m);

%Alternating minimization

for i=1:iterations
    if(mod(i,2) == 0) %update U
        U = inverse(M'*M + lambda*I)*M'*Ratings
    else %update M
        M = inverse(U'*U + lambda*I)*U'*Ratings
    end
end

%Predict

PredictedRatings = U*M'

RMSE = sqrt(sum(sum( (PredictedRatings(testIdx)-Ratings(testIdx).^2) )))/length(testIdx);

%=======Crossvalidation=======

%We provide you with a matrix cvSet which contains indices for 10-fold Cross-validation set. Row cvSet(i, :) contains the indices for first cross-validation set. Thus, if you want to leave first set out and perform training on 2-10 sets, then you will type:
trR1=trR;
trR1(cvSet(1,:))=0;

%=======Plot RMSE=======

%=======Results=======

%optimal lambda

%problems with lambda=0

%RMSE for optimal lambda
