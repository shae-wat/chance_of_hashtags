function [U,M] = alt_min(R, lambda)

    %u = 1978; %number users
    u = size(R,1);
    %m=4635; %number movies
    m = size(R,2);
    k = 10; %number genres
    iterations = 30;
    I = eye(k,k);

    U = randn(u,k);
    M = randn(m,k);

    for iteration=1:iterations
        if(mod(iteration,2) == 0) %=====update U
            %for each user
            for i=1:u
                %r=user who rated movie
                %v=rating
                [Rur,Ruc,Ruv] = find(R(i,:));
                Mk = M(Ruc, :);
                U(i,:) = inv(Mk'*Mk + lambda*I)*Mk'*Ruv';
            end
        else %=====update M
            %for each movie
            for j=1:m
                %r=user who rated movie
                %v=rating
                [Rr,Rc,Rv] = find(R(:,j));
                Uk = U(Rr, :);
                M(j,:) = inv(Uk'*Uk + lambda*I)*Uk'*Rv;
            end
        end
    end

end
