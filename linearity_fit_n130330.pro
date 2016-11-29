cd,'/Users/ktmorz/home/research_reorg/magao/clio/linearity'
path30 = 'n130330/'
cube = readclio(path30, 'linearity', findgen(21)+1, head=head)
nim = (size(cube))[3]
ints = fltarr(nim) & for k=0,nim-1 do ints[k] = sxpar(head[*,k],'INT')
print,ints

rectanglemask = fltarr(400,200)
rectanglemask[200:350,0:*]=1.0
counts = fltarr(nim)
for k=0,nim-1 do begin im=cube[*,*,k]  &  counts[k]=median(im[where(rectanglemask eq 1)])
print,counts

n_int = n_elements(uniq(ints))
stddevmean = fltarr(n_int)
ints_uniq = ints[uniq(ints)]
print,ints_uniq
print,n_int

for k=0,n_int-1 do stddevmean[k] = stddev(counts[where(ints eq ints_uniq[k])])/mean(counts[where(ints eq ints_uniq[k])])
print,stddevmean

counts_mean = fltarr(n_int)
for k=0,n_int-1 do counts_mean[k] = mean(counts[where(ints eq ints_uniq[k])])
print,counts_mean

counts_stddev = fltarr(n_int)
for k=0,n_int-1 do counts_stddev[k] = stddev(counts[where(ints eq ints_uniq[k])])
print,counts_stddev

psplot_start, 'lin_data.eps'
plot,ints,counts,psym=1, xtitle='Ints (ms)',ytitle='Counts (DN)'
psplot_stop

ints_true_coeff = linfit(ints_uniq, counts_mean)
psplot_start, 'lin_data_fit.eps'
plot,ints,counts,psym=1, xtitle='Ints (ms)',ytitle='Counts (DN)'
oplot,ints_uniq,ints_true_coeff[0]+ints_uniq*ints_true_coeff[1],thick=2
psplot_stop

psplot_start,'lin_data_true_meas.eps'
plot,counts_true, counts_mean,psym=1, xtitle='True Counts (DN)',ytitle='Measured Counts (DN)'
psplot_stop

ints_true_coeff = linfit(ints_uniq[where(ints_uniq gt 500 and ints_uniq lt 2000)],counts_mean[where(ints_uniq gt 500 and ints_uniq lt 2000)])
counts_true = ints_true_coeff[0]+ints_uniq*ints_true_coeff[1]
print,counts_mean
print,counts_true
print,ints_true_coeff

psplot_start, 'lin_data_fit_500_2000.eps'
plot,ints,counts,psym=1, xtitle='Ints (ms)',ytitle='Counts (DN)'
oplot,ints_uniq,ints_true_coeff[0]+ints_uniq*ints_true_coeff[1],thick=2
psplot_stop


print,counts_mean
print,counts_true
idx = where(counts_true gt 1e4 and counts_true lt 3e4)
;idx = where(counts_mean gt 1e4 and counts_mean lt 4e4)
print,idx
print,counts_mean[idx]
print,counts_true[idx]

xarr = findgen(6000)*10.

coeff1 = linfit(counts_true[idx], counts_mean[idx])
print,coeff1
yarr1 = coeff1[0] + coeff1[1]*xarr
print,counts_fit1

coeff2 = poly_fit(counts_true[idx], counts_mean[idx], 2)
print,coeff2
yarr2 = coeff2[0] + coeff2[1]*xarr + coeff2[2]*(xarr^2.)
print,counts_fit2

coeff3 = poly_fit(counts_true[idx], counts_mean[idx], 3)
print,coeff3
yarr3 = coeff3[0] + coeff3[1]*xarr + coeff3[2]*(xarr^2.) + coeff3[3]*(xarr^3.)
print,counts_fit3

coeff4 = poly_fit(counts_true[idx], counts_mean[idx], 4)
print,coeff4
yarr4 = coeff4[0] + coeff4[1]*xarr + coeff4[2]*(xarr^2.) + coeff4[3]*(xarr^3.) + coeff4[4]*(xarr^4.)
print,counts_fit4

psplot_start,'lin_fit.eps',/color
plot,counts_true, counts_mean,psym=1, xtitle='True Counts (DN)',ytitle='Measured Counts (DN)'
oplot, xarr, yarr1,linestyle=0,thick=4, color=fsc_color('orange')
oplot, xarr, yarr2,linestyle=0,thick=4, color=fsc_color('red')
oplot, xarr, yarr3,linestyle=0,thick=4, color=fsc_color('green')
oplot, xarr, yarr4,linestyle=0,thick=4, color=fsc_color('purple')
oplot,counts_true, counts_mean,psym=1,thick=4,symsize=2
al_legend,['Linear fit','2nd-order poly fit','3rd-order poly fit','4th-order poly fit'],$
color=[fsc_color('orange'),fsc_color('red'),fsc_color('green'),fsc_color('purple')],linestyle=[0,0,0,0],thick=[4,4,4,4],/top,/left
psplot_stop
