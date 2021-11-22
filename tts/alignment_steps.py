import matplotlib.pyplot as plt

def do_visualize(alignment_history):
  fig = plt.figure(figsize=(8, 6))
  ax = fig.add_subplot(111)
  # 解码编码对齐时间阶梯图
  ax.set_title(f'Alignment steps')
  im = ax.imshow(
      alignment_history,
      aspect='auto',
      origin='lower',
      interpolation='none')
  fig.colorbar(im, ax=ax)
  # 解码时间
  xlabel = 'Decoder timestep'
  plt.xlabel(xlabel)
  # 编码时间
  plt.ylabel('Encoder timestep')
  plt.tight_layout()
  plt.show()
  plt.close()
