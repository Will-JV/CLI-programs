function runge(l,u,w)%l = lower,u = upper, w = width
n = (u-l)/w;        %n is the number of columns
x = zeros(1,n);     %Intializing matrix
y = zeros(1,n);
y(1,1) = 1;
l = l + w;
for i = 2:n+1
    x(1,i) = l;
    temp = y(1,i-1);
    k1 = temp;
    k2 = temp + w*k1/2;
    k3 = temp + w*k2/2;
    k4 = temp + w*k3;
    y(1,i) = temp + w*(k1 + 2*k2 + 2*k3 + k4)/6;
    l = l + w;
end
plot(x,y)    
end
