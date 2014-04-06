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

R = nonzeros(Ratings);
U = randn(u,k);
Uk = nonzeros(U);
M = randn(m,k);
Mk = nonzeros(M);

%Alternating minimization

for iteration=1:iterations
    if(mod(i,2) == 0) %update U
        U = inverse(Mk'*Mk + lambda*I)*Mk'*R
    else %update M
        %redefinecolumns of M
        for j=1:size(M,2);
            M(:,j) = inverse(Uk(:,j)'*Uk(:,j) + lambda*I)*Uk(:,j)'*R(:,j)
        end
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
