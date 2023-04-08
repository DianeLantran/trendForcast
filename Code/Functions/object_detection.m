
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% object detection
%
% [colorHist] = object_detection( PROJ_D , filename , LogId, colorhist )
%
%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%ENTREES%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%
%
%   PROJ_D  % Root directory of the project
%
%   kpack  : identyfying number of the package
%            1  Database Drive (train set)
%
%   filename_in : full image filename
%
%
%   LogId    : (Optional) ID of the LOG file (> 2) /Display (1) / Nothing (0)
%               Default : 0
%
%   colorHist    : array filled with the colored catched by the analysis
%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%SORTIES%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%
%
%
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% object_detection.m
% Diane Lantran
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



function [colorHist] = object_detection( PROJ_D , kpack, filename_in , LogId, colorHist)

%% Parameters

flag_display    = false;%true;% flag of display




%% Image name



[~,im_name_in] = fileparts(filename_in);


%% Program

%% try : to intercept the errors
%try



% image file
im = imread(filename_in);


if flag_display
    
    figure();
    imagesc(im); colormap gray; hold on;
    title(sprintf('image %s',im_name_in));
    axis equal
end

 % extraction of the green component
im_G = double(imadjust(rgb2gray(im)));



if flag_display
    
    figure();
    imagesc(im_G); colormap gray; hold on;
    title('Green component');
    axis equal
end

%% segmentation of the ZOI (Zone of interest)

h = fspecial('gaussian');
im_Glisse= filter2(h, im_G);
%im_G = graythresh(im_G);

sigma=1;
method='sobel';
[g1,gh1,gv1]=tse_imgrad(im_Glisse,method,sigma); % gradiant suivant la méthode de Sobel
[g high]=tse_imhysthreshold(g1, 10, 2); % seuil haut = 20 : on ne garde que les contours
%g = imbinarize(g);
g = bwareaopen(g, 60); %suppression des objets d'aire inférieure à 60 pixels

gf=imfill(g, 'holes'); %on remplit le contour
gf = imclose(gf, strel('disk', 10));
gf = imfill(gf, 'holes');
msk_ZOI = gf;
msk_ZOI=msk_ZOI > 0;


if flag_display
    
    figure();
    imagesc(msk_ZOI); colormap gray; hold on;
    title('My segmentation of the ZOI!!!');
    axis equal
end


%% segmentation of the objects

% Mask the image using bsxfun() function
msk_object = bsxfun(@times, im, cast(msk_ZOI, 'like', im));

if flag_display
    
    figure();
    imagesc(msk_object); colormap gray; hold on;
    title('My segmentation of the vessels!!!');
    axis equal
end

%% Analysis of the segmented object

colorHist = color_detection(msk_object, colorHist);
%% Saving the results


kfile = 11; % Mask of the image Zone of Interest    
[fname] = TP_GEN_filenames( PROJ_D , kpack, kfile, filename_in);
ajout_dossier(fname);
imwrite( msk_ZOI , fname );
fprintf('<------------------- Saved : %s\n',fname);


kfile = 21; % vessels_mask
[fname] = TP_GEN_filenames( PROJ_D , kpack, kfile, filename_in);
ajout_dossier(fname);
imwrite( msk_object , fname );
fprintf('<------------------- Saved : %s\n',fname);

%% Superimposition of the boundary of the mask vessels to the image
if 1
    boundary_vessels = bwboundaries(im_G .* msk_ZOI);
    im_R = im(:,:,1);
    im_G = im(:,:,2);
    im_B = im(:,:,3);
    SZ = size(im);
    for n=1:length(boundary_vessels)
       bv_ij = boundary_vessels{n};
       ind = sub2ind( SZ(1:2) , bv_ij(:,1) , bv_ij(:,2) );
       im_R(ind) = 255;
       im_G(ind) = 255;
       im_B(ind) = 255;
    end
    im_col_out = cat(3,im_R,im_G,im_B);
    
    
    kfile = 22; % vessels_mask superimposed on the image
    [fname] = TP_GEN_filenames( PROJ_D , kpack, kfile, filename_in);
    imwrite( im_col_out , fname );
    fprintf('<------------------- Saved : %s\n',fname);
    
    
    if flag_display

        figure();
        imagesc(im_col_out); colormap gray; hold on;
        title('Boundaries of the vessels!');
        axis equal
    end
end

if flag_display
   pause(5);% a pause of 5 seconds
   close all;
end

%% Catch : to write the error message in the Log file

% %% Error management
% catch ME
%     EvenementLOG(LogId, 1, ME.message, 1);
% end
