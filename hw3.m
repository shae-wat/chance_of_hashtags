%hw3

load hw3_netflix.mat
warning('off');

%alt_min.m contains learning function

%Loop over lambdas
lambdas = [0: 0.05: 1];
lambda_av_rmse = randn(length(lambdas),1); %hold averaged lambda results
for l = 1:length(lambdas)
    lambda = lambdas(1,l)

	%=======Crossvalidation=======

	total_RMSE = 0;
	for crossSet = 1:size(cvSet,1)
		%select cross validation set
		trRc=trR;
		trRc(cvSet(crossSet,:))=0;
		[U1,M1] = alt_min(trRc, lambda); %alternating minimization on this set with this lambda value
		PredictedRatingc = U1*M1';
		RMSEc = sqrt(sum(sum((PredictedRatingc(cvSet(crossSet,:))-trR(cvSet(crossSet,:))).^2))/length(cvSet(crossSet,:)));
	
		%total RMSE for this lambda
		total_RMSE = total_RMSE + RMSEc;
	end
	%average RMSE for this lambda
	av_RMSE = total_RMSE/10
	lambda_av_rmse(l) = av_RMSE;

end

%=======Plot=======

plot(lambdas, lambda_av_rmse)


