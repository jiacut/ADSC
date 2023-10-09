clc;clear;

figure('position', [150, 100, 450, 350]);


% ׼������
theta = 0.3: 0.1 :0.9;
beta = 0.3: 0.1 :0.9;

Z = [0.573	0.58	0.588	0.583	0.578	0.575	0.569
0.589	0.592	0.612	0.603	0.597	0.586	0.582
0.624	0.635	0.648	0.639	0.632	0.626	0.62
0.676	0.682	0.695	0.69	0.683	0.677	0.67
0.687	0.693	0.708	0.701	0.698	0.692	0.685
0.692	0.708	0.716	0.71	0.702	0.695	0.691
0.706	0.718	0.725	0.722	0.716	0.71	0.704];


% ����������ɫ,��ɫΪRGB��ԭɫ
color_matrix = [0,255,255;255,127,80;160,102,211;50,205,50;80,80,255;240,230,140;255,68,0]/255;

% ����״ͼ
h = bar3(Z', 0.7);
axis([-inf inf -inf inf min(Z(:))*0.95 max(Z(:))*1.1]);
for n = 1:numel(h)
    cdata = get(h(n), 'zdata');
    set(h(n), 'cdata', cdata, 'facecolor', color_matrix(n,:));
end

% ����С��ǩ
yLabelName = arrayfun(@(x) num2str(x), theta, 'UniformOutput', false);
xLabelName = arrayfun(@(x) num2str(x), beta, 'UniformOutput', false);
set(gca, 'yticklabel',yLabelName,'Fontname','Times New Roman','FontSize',8);
set(gca, 'xticklabel',xLabelName,'Fontname','Times New Roman','FontSize',8);

% �޸�ÿ����ı�ǩ
ylabel('\theta', 'Fontname', '����', 'FontSize', 10);
xlabel('\beta', 'Fontname', '����', 'FontSize', 10);
zlabel('NMI', 'Fontname', '����', 'FontSize', 10);


% legend({'0.01','0.05','0.1','1','10','50','100'});
