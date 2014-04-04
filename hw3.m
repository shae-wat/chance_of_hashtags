%hw3

load hw3_netflix.mat

%=======Assignment parameters=======
u = 1978; %number users
m=4635; %number movies
k = 10; %number genres
iterations = 30;
lambda = 0.5; %****
I = eye(k,k) %****

%=======Learn M and U given R=======

U = randn(u,k);
M = randn(k,m);

%Alternating minimization

for i=1:iterations
    if(i%2 == 0) %update M
        M = inv(U'*U + lambda*I)*U'*Ratings
    else %update U
        U = inv(M'*M + lambda*I)*M'*Ratings
    end
end

%Predict

PredictedRatings = U*M'

RMSE = sqrt(sum(sum( (PredictedRatings(testIdx)-Ratings(testIdx).^2) )))/length(testIdx);

%=======Crossvalidation=======

%=======Plot RMSE=======

%=======Results=======

%optimal lambda

%problems with lambda=0

%RMSE for optimal lambda
