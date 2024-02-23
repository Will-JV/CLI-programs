function runge(l,u,h)%l = lower,u = upper, h = width
    n = (u-l)/h;        %n is the number of columns
    t = zeros(1,n);      %Intializing matrix
    x1 = zeros(1,n);    
    x2 = zeros(1,n);
    x1(1) = 4;
    x2(1) = -7;

    for i = 1:n
        k1 = h*func1(x1(i),x2(1));
        k2 = h*func1(x1(i)+h/2,x2(i)+k1/2);
        k3 = h*func1(x1(i)+h/2,x2(i)+k2/2);
        k4 = h*func1(x1(i)+h,x2(i)+k3);

        x1(i+1) = x1(i) + (k1 + 2*k2 + 2*k3 + k4)/6;

        k1 = h*func2(x1(i),x2(1));
        k2 = h*func2(x1(i)+h/2,x2(i)+k1/2);
        k3 = h*func2(x1(i)+h/2,x2(i)+k2/2);
        k4 = h*func2(x1(i)+h,x2(i)+k3);

        x2(i+1) = x2(i) + (k1 + 2*k2 + 2*k3 + k4)/6;
        
        t(i+1) = t(i) + h;
    end
    hold on
    plot(t,x1)
    plot(t,x2)
    ezplot("0",[0,10])
    hold off    
end

function f = func1(x1,x2) %#ok<INUSL>
   f = x2;
end

function f = func2(x1,x2)
   f = -2*x2-10*x1;
end
