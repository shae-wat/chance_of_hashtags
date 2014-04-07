%hw3

load hw3_netflix.mat

%=======Assignment parameters=======
u = 1978; %number users
m=4635; %number movies
k = 10; %number genres
iterations = 30;
I = eye(k,k);

%=======Learn M and U given R=======
%Alternating minimization
function [U,M] = alt_min(R)
    U = randn(u,k);
    M = randn(m,k);

    lambda = 0.5;

    for iteration=1:iterations
        if(mod(iteration,2) == 0) %=====update U
            %for each user
            for i=1:size(R,1)
                %r=user who rated movie
                %v=rating
                [Rur,Ruc,Ruv] = find(R(i,:));
                Mk = M(Rur, :);
                
                U(i,:) = inv(Mk'*Mk + lambda*I)*Mk'*Ruv';
            end
        else %=====update M
            %for each movie
            for j=1:size(R,2)
                %r=user who rated movie
                %v=rating
                [Rr,Rc,Rv] = find(R(:,j));
                Uk = U(Rr, :);
                
                M(j,:) = inv(Uk'*Uk + lambda*I)*Uk'*Rv;
            end
        end
    end

    %Predict
    PredictedRatings = U*M';

    RMSE = sqrt(sum(sum( (PredictedRatings(testIdx)-Ratings(testIdx).^2) )))/length(testIdx);

end
%=======Crossvalidation=======


trR1=trR;
trR1(cvSet(1,:))=0;
 %Now you train using trR1 data and after you find out the solution matrix U1 and M1, calculate RMSE using:
[U1,M1] = alt_min(trR1);
PredictedRatings1 = U1*M1';
RMSE1 = sqrt(sum(sum((PredictedRatings1(cvSet(1,:))-trR(cvSet(1,:))).^2))/length(cvSet(1,:)))

%=======Plot RMSE=======

%=======Results=======

%optimal lambda

%problems with lambda=0

%RMSE for optimal lambda
