function euler(l,u,w) %l = lower,u = upper, w = width
n = (u-l)/w;        %n is the number of columns
x = zeros(1,n);     %Intializing matrix
y = zeros(1,n);
y(1,1) = 1;         
l = l + w;
for i = 2:n
    x(1,i) = l;
    y(1,i) = exp(-l)-w*exp(-l);
    l = l + w;
end
plot(x,y)    
end
  
