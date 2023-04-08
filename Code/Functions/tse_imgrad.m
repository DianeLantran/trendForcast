function [g,gh,gv]=tse_imgrad(f,method,sigma)
% Calcule les gradients horizonatux et verticaux de f en utilisant la méthode précisée en paramètre :
% sobel ou gog (gradient of gaussian). Ensuite cherche le maximum du gradient et le retourne.

if nargin<2, method='sobel';end
if nargin<3, sigma=1;end

% Si la méthode renseignée est 'sobel'
if strcmp(method,'sobel')
    gh = imfilter(double(f),fspecial('sobel')' /8,'replicate');
    gv = imfilter(double(f),fspecial('sobel')/8,'replicate');

% Si la méthode renseignée est 'gog'
elseif strcmp(method,'gog')
    width=ceil(4*sigma);
    ssq=sigma^2;
    x=-width:width;
    gau = exp(-(x.*x)/(2*ssq))/(2*pi*ssq);     % construction d'un filtre gaussien 1D
    dgau = -x.*exp(-(x.*x)/(2*ssq))/ssq;  % the 1D first derivative of gaussian filter
    gh=imfilter(double(f),gau','replicate');
    gh=imfilter(gh,dgau,'replicate');
    gv=imfilter(double(f),gau,'replicate');
    gv=imfilter(gv,dgau','replicate');

else error('incorrect method');
end

% Detect local maxima of the gradient in the direction of the gradient
% vector
g=tse_imdetectmaxgrad(gh,gv);

end