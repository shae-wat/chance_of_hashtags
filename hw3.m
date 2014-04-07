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

%R = nonzeros(Ratings)
U = randn(u,k);
M = randn(m,k);


%Alternating minimization

for iteration=1:iterations
    if(mod(iteration,2) == 0) %=====update U
        %for each user
        for i=1:size(Ratings,1)
            %r=user who rated movie
            %v=rating
            [Rur,Ruc,Ruv] = find(Ratings(i,:));
            Mk = M(Rur, :);
            
            U(i,:) = inv(Mk'*Mk + lambda*I)*Mk'*Ruv;
        end
    else %=====update M
        %for each movie
        for j=1:size(Ratings,2)
            %r=user who rated movie
            %v=rating
            [Rr,Rc,Rv] = find(Ratings(:,j));
            Uk = U(Rr, :);
            
            M(j,:) = inv(Uk'*Uk + lambda*I)*Uk'*Rv;
        end
    end
end

%Predict

PredictedRatings = U*M';

%RMSE = sqrt(sum(sum( (PredictedRatings(testIdx)-Ratings(testIdx).^2) )))/length(testIdx);

%=======Crossvalidation=======

%We provide you with a matrix cvSet which contains indices for 10-fold Cross-validation set. Row cvSet(i, :) contains the indices for first cross-validation set. Thus, if you want to leave first set out and perform training on 2-10 sets, then you will type:
%trR1=trR;
%trR1(cvSet(1,:))=0;

%=======Plot RMSE=======

%=======Results=======

%optimal lambda

%problems with lambda=0

%RMSE for optimal lambda
