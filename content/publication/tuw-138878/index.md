---
abstract: 'Purpose: The accurate determination of the central vessel axis is a prerequisite
  for automated visualization (curved planar reformation) and quantitation. The purpose
  of this work was to assess the accuracy of different algorithms for automated centerline
  detection in a phantom simulating the peripheral arterial tree. Methods and Material:
  Six algorithms were used to determine the centerline of a synthetic peripheral arterial
  vessel (aorto-to-pedal arteries, diameter 18-0.6mm) dataset (256x256x600, voxel
  size 0.5x0.5x0.5mm). They are ray-casting/thresholding (RCT), ray-casting/maximum
  gradient (RCMG), block matching (BM), fitting to ellipse (FE), center of gravity
  (CoG), and Randomized Hough transform (RHT). Gaussian noise whith a sigma: 0, 5
  and 10 was used to observe the accuracy of the method under noise influence The
  accuracy of automatic centerline determination was quantified by measuring the error-distance
  between the derived centerlines, and the known centerline course of the synthetic
  dataset. Results: BM demonstrated unacceptable performance in large vessels (>5mm)
  when the shift used was less than 3 voxels. RCMG demonstrated a greater error (mean
  of the error 4.73mm) in large diameter (>15mm) vessels than in small diameter (<15mm)
  vessels (mean of the error 0.64mm). Because RHT and FE use Canny edge detector preprocessing,
  both are sensitive to noise. CoG and RCT keep the mean of the error-distance significantly
  smaller (0.7mm and 0.9mm respectively) than all other algorithms. Conclusion: CoG
  and RCT algorithms provide the most efficient centerline approximation over a wide
  range of vessel diameters.'
authors:
- Alexandra LaCruz
- Matus Straka
- A Köchl
- Milos Sramek
- Eduard Gröller
- Dominik Fleischmann
date: '2004-01-01'
featured: false
links:
- name: Publik
  url: https://publik.tuwien.ac.at/showentry.php?ID=138878&lang=1
publication_types:
- '1'
publishDate: '2004-01-01'
title: Accuracy of Automated Centerline Approximation Algorithms for Lower Extremity
  Vessels in CTA Phantom
url_pdf: ''
---