T = 1:50;
x=0.00082;
k=x;
p(1)=9.6;
for i = 1:49
    p(i+1) = k*(665-p(i))*p(i)+p(i);
end
figure
scatter(T(1:20),p(1:20),500,'k.','LineWidth',20)